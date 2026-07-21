import networkx as nx
from typing import Dict, Any, List, Optional
from app.seed_data.seed_data import SAMPLE_KNOWLEDGE_GRAPH
from app.models.schemas import KnowledgeGraphData, GraphNode, GraphEdge, TimeTravelGraphResponse

class KnowledgeGraphService:
    def __init__(self):
        self.graph = nx.DiGraph()
        self._initialize_graph()

    def _initialize_graph(self):
        for node in SAMPLE_KNOWLEDGE_GRAPH["nodes"]:
            self.graph.add_node(node["id"], **node)
        for edge in SAMPLE_KNOWLEDGE_GRAPH["edges"]:
            self.graph.add_edge(edge["source"], edge["target"], **edge)

    def get_full_graph(self) -> Dict[str, Any]:
        nodes = []
        for n, data in self.graph.nodes(data=True):
            nodes.append(GraphNode(
                id=n,
                label=data.get("label", n),
                type=data.get("type", "Entity"),
                attributes=data.get("attributes", {})
            ))

        edges = []
        for u, v, data in self.graph.edges(data=True):
            edges.append(GraphEdge(
                source=u,
                target=v,
                type=data.get("type", "RELATED_TO"),
                attributes=data.get("attributes", {})
            ))

        return {"nodes": [n.dict() for n in nodes], "edges": [e.dict() for e in edges]}

    def filter_graph_by_query(self, query: str) -> Dict[str, Any]:
        q = query.lower()
        matching_nodes = set()
        for n, data in self.graph.nodes(data=True):
            if q in n.lower() or q in data.get("label", "").lower() or q in data.get("type", "").lower():
                matching_nodes.add(n)
                matching_nodes.update(self.graph.neighbors(n))
                matching_nodes.update(self.graph.predecessors(n))

        if not matching_nodes:
            return self.get_full_graph()

        sub = self.graph.subgraph(matching_nodes)
        nodes = [GraphNode(id=n, label=d.get("label", n), type=d.get("type", "Entity"), attributes=d.get("attributes", {})).dict() for n, d in sub.nodes(data=True)]
        edges = [GraphEdge(source=u, target=v, type=d.get("type", "RELATED_TO"), attributes=d.get("attributes", {})).dict() for u, v, d in sub.edges(data=True)]
        return {"nodes": nodes, "edges": edges}

    def compute_shortest_failure_path(self, source_id: str, target_id: str) -> List[str]:
        if source_id in self.graph and target_id in self.graph:
            try:
                return nx.shortest_path(self.graph, source=source_id, target=target_id)
            except (nx.NetworkXNoPath, nx.NodeNotFound):
                return [source_id, target_id]
        return [source_id, target_id]

    def compute_graph_centrality(self) -> Dict[str, float]:
        if len(self.graph) == 0:
            return {}
        centrality = nx.degree_centrality(self.graph)
        return {k: round(v, 4) for k, v in centrality.items()}

    def get_time_travel_snapshot(self, year: int) -> TimeTravelGraphResponse:
        all_graph = self.get_full_graph()
        
        if year <= 2022:
            filtered_nodes = [n for n in all_graph["nodes"] if n["id"] in ["P-101", "T-301", "DOC-101", "VEND-01"]]
            filtered_edges = [e for e in all_graph["edges"] if e["source"] in ["P-101", "T-301"] and e["target"] in ["P-101", "T-301", "DOC-101", "VEND-01"]]
            summary = f"Year {year}: Baseline Plant Commissioning (P-101 & T-301 online)."
        elif year <= 2024:
            filtered_nodes = [n for n in all_graph["nodes"] if n["id"] in ["P-101", "V-101", "T-301", "M-102", "DOC-101", "VEND-01", "ENG-01"]]
            filtered_edges = [e for e in all_graph["edges"] if e["source"] != "DOC-102" and e["target"] != "DOC-102"]
            summary = f"Year {year}: Expansion of Steam Header Control Valve V-101 and Motor M-102."
        else:
            filtered_nodes = all_graph["nodes"]
            filtered_edges = all_graph["edges"]
            summary = f"Year {year}: Full plant connected topology including high vibration incident reports & ISO asset telemetry."

        return TimeTravelGraphResponse(
            year=year,
            graph=KnowledgeGraphData(
                nodes=[GraphNode(**n) for n in filtered_nodes],
                edges=[GraphEdge(**e) for e in filtered_edges]
            ),
            diff_summary=summary
        )

    def add_or_merge_node(self, node_id: str, label: str, node_type: str, attributes: Dict[str, Any] = None):
        attrs = attributes or {}
        if node_id in self.graph:
            # Merge attributes
            self.graph.nodes[node_id].update(attrs)
        else:
            self.graph.add_node(node_id, label=label, type=node_type, attributes=attrs)

    def add_relationship(self, source: str, target: str, rel_type: str, attributes: Dict[str, Any] = None):
        if source in self.graph and target in self.graph:
            self.graph.add_edge(source, target, type=rel_type, attributes=attributes or {})

    def add_document_nodes(self, processed_doc: Dict[str, Any]):
        doc_id = processed_doc.get("id", f"DOC-{hash(processed_doc.get('filename', 'doc')) % 100000:05d}")
        self.add_or_merge_node(doc_id, processed_doc.get("filename", "Doc"), "Document", {"summary": processed_doc.get("summary", "")})

        for asset in processed_doc.get("extracted_assets", []):
            asset_id = asset["id"]
            self.add_or_merge_node(asset_id, asset.get("name", asset_id), "Asset", {"health": asset.get("health", 85.0)})
            self.add_relationship(doc_id, asset_id, "MENTIONS")

kg_service = KnowledgeGraphService()
