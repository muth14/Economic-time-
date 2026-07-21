from app.services.knowledge_graph import kg_service

def test_knowledge_graph_traversal():
    graph_data = kg_service.get_full_graph()
    assert len(graph_data["nodes"]) > 0
    assert len(graph_data["edges"]) > 0

def test_graph_query_filter():
    filtered = kg_service.filter_graph_by_query("P-101")
    assert len(filtered["nodes"]) > 0
    node_ids = [n["id"] for n in filtered["nodes"]]
    assert "P-101" in node_ids

def test_graph_shortest_path():
    path = kg_service.compute_shortest_failure_path("M-102", "P-101")
    assert len(path) >= 2
    assert path[0] == "M-102"
    assert path[-1] == "P-101"

def test_graph_time_travel_snapshot():
    snapshot_2021 = kg_service.get_time_travel_snapshot(2021)
    snapshot_2026 = kg_service.get_time_travel_snapshot(2026)
    assert snapshot_2021.year == 2021
    assert snapshot_2026.year == 2026
    assert len(snapshot_2026.graph.nodes) >= len(snapshot_2021.graph.nodes)
