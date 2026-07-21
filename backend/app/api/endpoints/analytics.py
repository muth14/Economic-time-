from fastapi import APIRouter
from typing import Dict, Any

router = APIRouter()

@router.get("/summary", response_model=Dict[str, Any])
def get_analytics_summary():
    return {
        "total_assets": 128,
        "active_monitored_sensors": 1420,
        "indexed_documents": 3480,
        "knowledge_graph_triples": 24500,
        "avg_plant_health_index": 82.4,
        "active_critical_alerts": 2,
        "prevented_downtime_hours_this_month": 48.5,
        "estimated_cost_savings_usd": 640000.0,
        "downtime_trend": [
            {"month": "Jan", "unplanned_hours": 12.0, "planned_hours": 24.0},
            {"month": "Feb", "unplanned_hours": 8.5, "planned_hours": 18.0},
            {"month": "Mar", "unplanned_hours": 15.0, "planned_hours": 30.0},
            {"month": "Apr", "unplanned_hours": 4.2, "planned_hours": 16.0},
            {"month": "May", "unplanned_hours": 2.0, "planned_hours": 20.0},
            {"month": "Jun", "unplanned_hours": 1.1, "planned_hours": 14.0},
            {"month": "Jul", "unplanned_hours": 0.5, "planned_hours": 12.0}
        ],
        "failure_category_breakdown": [
            {"category": "Bearing & Lubrication", "count": 42},
            {"category": "Seal Flushing Leakage", "count": 28},
            {"category": "Valve Actuator Jam", "count": 19},
            {"category": "Electrical Insulation", "count": 12},
            {"category": "Structural Corrosion", "count": 8}
        ]
    }
