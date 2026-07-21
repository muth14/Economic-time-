from fastapi import APIRouter
from typing import List, Dict, Any
from app.models.schemas import WhatIfRequest, WhatIfResponse, SOPRequest, SOPResponse, RiskRadarData
from app.services.predictive_engine import predictive_service
from app.seed_data.seed_data import SAMPLE_ASSETS

router = APIRouter()

@router.get("/assets", response_model=List[Dict[str, Any]])
def list_predictive_assets():
    return SAMPLE_ASSETS

@router.get("/heatmap", response_model=List[Dict[str, Any]])
def get_risk_heatmap():
    return predictive_service.get_plant_risk_heatmap()

@router.post("/what-if", response_model=WhatIfResponse)
def simulate_what_if(payload: WhatIfRequest):
    return predictive_service.simulate_what_if_failure(payload.trigger_entity_id, payload.failure_mode)

@router.post("/sop", response_model=SOPResponse)
def generate_sop(payload: SOPRequest):
    return predictive_service.generate_sop(payload.asset_id, payload.procedure_type)

@router.get("/risk-radar", response_model=RiskRadarData)
def get_risk_radar():
    return predictive_service.get_risk_radar()
