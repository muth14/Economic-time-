from fastapi import APIRouter, Query
from app.services.knowledge_graph import kg_service
from app.models.schemas import KnowledgeGraphData, TimeTravelGraphResponse

router = APIRouter()

@router.get("/", response_model=dict)
def get_graph(query: str = None):
    if query:
        return kg_service.filter_graph_by_query(query)
    return kg_service.get_full_graph()

@router.get("/time-travel", response_model=TimeTravelGraphResponse)
def get_graph_time_travel(year: int = Query(2026, ge=2020, le=2026)):
    return kg_service.get_time_travel_snapshot(year)
