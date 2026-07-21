from fastapi import APIRouter
from app.models.schemas import CopilotQuery, CopilotResponse, ExplainabilityDashboardData
from app.services.RAG_engine import rag_service

router = APIRouter()

@router.post("/query", response_model=CopilotResponse)
def ask_industrial_copilot(payload: CopilotQuery):
    return rag_service.search_and_reason(payload.query, asset_id=payload.asset_id)

@router.get("/explainability/{query_id}", response_model=ExplainabilityDashboardData)
def get_query_explainability(query_id: str):
    return ExplainabilityDashboardData(
        query_id=query_id,
        sources_used=[
            {"doc_id": "DOC-102", "doc_name": "P101_Vibration_Anomaly_Incident_Report.pdf", "page": 3, "weight": 0.45},
            {"doc_id": "DOC-101", "doc_name": "Pump_P101_OEM_Manual.pdf", "page": 14, "weight": 0.35},
            {"doc_id": "DOC-103", "doc_name": "P_AND_ID_Boiler_Feed_System_Rev4.pdf", "page": 1, "weight": 0.20}
        ],
        graph_traversal_path=[
            "Entity Node: [P-101]",
            "Edge: [P-101] -> FAILED_DUE_TO -> [DOC-102]",
            "Edge: [P-101] -> MAINTAINED_BY -> [Eng. Elena Rostova]",
            "Edge: [P-101] -> USES -> [Flowserve API Plan 53B]"
        ],
        agent_contributions=[
            {"agent": "Knowledge Agent", "contribution": "Retrieved 3 vector chunks and 6 graph nodes"},
            {"agent": "Failure Analysis Agent", "contribution": "Identified drive-end bearing micro-pitting root cause"},
            {"agent": "Compliance Agent", "contribution": "Verified OISD-137 maintenance periodicity standard"}
        ],
        confidence_breakdown={
            "Vector Similarity Score": 0.94,
            "Graph Neighborhood Density": 0.92,
            "Document Recency Index": 0.98,
            "Composite Trust Score": 94.8
        },
        timeline_evidence=[
            {"date": "2026-05-10", "evidence": "Mechanical Seal Cartridge Replacement by Eng. Elena Rostova"},
            {"date": "2026-07-12", "evidence": "Vibration Anomaly Event (6.8 mm/s Peak RMS)"}
        ]
    )
