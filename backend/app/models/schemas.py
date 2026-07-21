from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

# --- Auth Schemas ---
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: Dict[str, Any]

class UserLogin(BaseModel):
    username: str
    password: str

# --- Document Intelligence Schemas ---
class EntityExtracted(BaseModel):
    category: str
    value: str
    confidence: float
    bbox: Optional[List[float]] = None

class DocumentResponse(BaseModel):
    id: str
    filename: str
    file_type: str
    upload_time: str
    status: str
    page_count: int
    entities: List[EntityExtracted]
    summary: str
    risk_level: str

# --- Knowledge Graph Schemas ---
class GraphNode(BaseModel):
    id: str
    label: str
    type: str
    attributes: Dict[str, Any] = Field(default_factory=dict)

class GraphEdge(BaseModel):
    source: str
    target: str
    type: str
    attributes: Dict[str, Any] = Field(default_factory=dict)

class KnowledgeGraphData(BaseModel):
    nodes: List[GraphNode]
    edges: List[GraphEdge]

class TimeTravelGraphResponse(BaseModel):
    year: int
    graph: KnowledgeGraphData
    diff_summary: str

# --- Copilot & Enterprise RAG Schemas ---
class CopilotQuery(BaseModel):
    query: str
    asset_id: Optional[str] = None
    voice_input: bool = False
    filters: Dict[str, Any] = Field(default_factory=dict)

class Citation(BaseModel):
    doc_id: str
    doc_name: str
    page: int
    snippet: str
    relevance_score: float

class CopilotResponse(BaseModel):
    answer: str
    reasoning_chain: List[str]
    root_cause: Optional[str] = None
    citations: List[Citation]
    timeline_events: List[Dict[str, Any]]
    recommended_actions: List[str]
    confidence_score: float  # Trust Meter (0-100)
    audio_response_url: Optional[str] = None

# --- RCA Agent Schemas ---
class FishboneCategory(BaseModel):
    category: str  # e.g. Machine, Method, Material, Manpower, Measurement, Environment
    causes: List[str]

class RCARequest(BaseModel):
    incident_id: str
    asset_id: str

class RCAResponse(BaseModel):
    incident_title: str
    asset_id: str
    fishbone: List[FishboneCategory]
    five_whys: List[Dict[str, str]]
    timeline: List[Dict[str, str]]
    recommended_fixes: List[str]
    preventive_actions: List[str]

# --- Predictive Maintenance Schemas ---
class AssetHealthScore(BaseModel):
    asset_id: str
    asset_name: str
    category: str
    location: str
    rul_days: int
    failure_probability: float
    risk_score: float
    status: str  # Critical, Warning, Normal
    next_maintenance_date: str

class RiskHeatmapCell(BaseModel):
    grid_id: str
    area_name: str
    asset_ids: List[str]
    risk_level: str  # Green, Yellow, Orange, Red
    avg_health_score: float

# --- Compliance Schemas ---
class ComplianceReport(BaseModel):
    report_id: str
    standard: str  # ISO 55001, OISD-137, PESO, Factory Act
    compliance_score: float
    violations_detected: List[Dict[str, Any]]
    recommendations: List[str]
    audit_evidence_files: List[str]

# --- Asset Digital Twin Schemas ---
class DigitalTwinDetail(BaseModel):
    asset_id: str
    name: str
    type: str
    location: str
    status: str
    specifications: Dict[str, Any]
    telemetry: Dict[str, Any]
    connected_assets: List[str]
    active_risk_score: float
    documents: List[Dict[str, str]]
    recent_maintenance: List[Dict[str, Any]]

class EquipmentChatQuery(BaseModel):
    asset_id: str
    message: str

# --- Hackathon Innovation Schemas ---
class WhatIfRequest(BaseModel):
    trigger_entity_id: str
    failure_mode: str  # e.g., "Complete Power Loss", "Seized Bearing", "Valve Jam"

class WhatIfCascadeStep(BaseModel):
    step: int
    entity_id: str
    entity_name: str
    impact_level: str  # Severe, High, Moderate, Low
    consequence: str
    time_to_impact: str

class WhatIfResponse(BaseModel):
    trigger_entity: str
    cascade_chain: List[WhatIfCascadeStep]
    total_plant_downtime_est_hours: float
    est_financial_loss_usd: float
    mitigation_strategy: List[str]

class SOPRequest(BaseModel):
    asset_id: str
    procedure_type: str  # Maintenance, Emergency Shutdown, Calibration

class SOPResponse(BaseModel):
    procedure_title: str
    asset_id: str
    steps: List[Dict[str, Any]]
    required_tools: List[str]
    safety_ppe: List[str]
    generated_at: str

class IndustrialWikiPage(BaseModel):
    asset_id: str
    title: str
    overview: str
    operating_parameters: Dict[str, Any]
    known_failure_modes: List[str]
    historical_modifications: List[str]
    ai_summary: str

class IncidentStoryResponse(BaseModel):
    incident_id: str
    title: str
    narrative_story: str
    involved_engineers: List[str]
    key_lessons: List[str]

class RiskRadarData(BaseModel):
    overall_enterprise_risk_index: float
    high_risk_assets: List[Dict[str, Any]]
    compliance_gap_count: int
    overdue_maintenances: int
    live_alerts: List[Dict[str, Any]]

# --- Final Innovation Enhancement Schemas ---
class EquipmentDNA(BaseModel):
    asset_id: str
    name: str
    category: str
    dna_fingerprint: str
    composite_health_index: float
    installation_date: str
    timeline: List[Dict[str, str]]
    maintenance_history: List[Dict[str, Any]]
    failure_history: List[Dict[str, Any]]
    compliance_history: List[Dict[str, Any]]
    ai_summary: str

class IndustrialMemoryInput(BaseModel):
    asset_id: str
    engineer_name: str
    feedback_correction: str
    verified_root_cause: str

class CrossPlantComparison(BaseModel):
    pattern_name: str
    analyzed_plants: List[str]
    affected_asset_types: List[str]
    common_failure_mode: str
    recurring_frequency: str
    recommended_global_action: str

class AIPlantDoctorBriefing(BaseModel):
    briefing_date: str
    overall_plant_status: str
    top_equipment_risks: List[Dict[str, Any]]
    predicted_total_downtime_hours: float
    active_compliance_issues: List[Dict[str, Any]]
    estimated_financial_loss_usd: float
    recommended_priority_actions: List[str]

class StrategyOption(BaseModel):
    strategy_name: str  # Run to Failure, Preventive Maintenance, Predictive Overhaul
    cost_usd: float
    downtime_hours: float
    risk_level: str
    estimated_savings_usd: float
    is_recommended: bool

class ExecutiveDecisionComparison(BaseModel):
    asset_id: str
    decision_title: str
    options: List[StrategyOption]
    optimal_recommendation: str

class ExplainabilityDashboardData(BaseModel):
    query_id: str
    sources_used: List[Dict[str, Any]]
    graph_traversal_path: List[str]
    agent_contributions: List[Dict[str, str]]
    confidence_breakdown: Dict[str, float]
    timeline_evidence: List[Dict[str, str]]

