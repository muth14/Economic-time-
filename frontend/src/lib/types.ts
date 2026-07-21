export interface Asset {
  id: string;
  name: string;
  type: string;
  category: string;
  location: string;
  status: 'Normal' | 'Warning' | 'Critical';
  health_score: number;
  rul_days: number;
  failure_probability: number;
  risk_level: 'Green' | 'Yellow' | 'Orange' | 'Red';
  specifications: Record<string, string>;
  telemetry: Record<string, string>;
  connected_assets: string[];
  recent_maintenance: Array<{ date: string; type: string; engineer: string; cost_usd: number }>;
  documents: Array<{ id: string; name: string; type: string }>;
}

export interface GraphNode {
  id: string;
  label: string;
  type: string;
  attributes?: Record<string, any>;
}

export interface GraphEdge {
  source: string;
  target: string;
  type: string;
  attributes?: Record<string, any>;
}

export interface KnowledgeGraphData {
  nodes: GraphNode[];
  edges: GraphEdge[];
}

export interface Citation {
  doc_id: string;
  doc_name: string;
  page: number;
  snippet: string;
  relevance_score: number;
}

export interface CopilotResponse {
  answer: string;
  reasoning_chain: string[];
  root_cause?: string;
  citations: Citation[];
  timeline_events: Array<{ time: string; event: string }>;
  recommended_actions: string[];
  confidence_score: number;
}

export interface HeatmapCell {
  grid_id: string;
  area_name: string;
  asset_ids: string[];
  risk_level: 'Green' | 'Yellow' | 'Orange' | 'Red';
  avg_health_score: number;
}
