from fastapi import APIRouter
from typing import Dict, Any, List
from app.models.schemas import IndustrialWikiPage, IncidentStoryResponse, IndustrialMemoryInput, CrossPlantComparison, AIPlantDoctorBriefing, ExecutiveDecisionComparison, StrategyOption
from app.services.agent_swarm import agent_swarm_service
from app.services.knowledge_graph import kg_service

router = APIRouter()

@router.get("/wiki/{asset_id}", response_model=IndustrialWikiPage)
def get_industrial_wiki(asset_id: str):
    return IndustrialWikiPage(
        asset_id=asset_id,
        title=f"Industrial Wiki: Asset {asset_id} (Boiler Feed Pump)",
        overview="High-pressure 3-stage centrifugal boiler feed pump manufactured by Flowserve Corp. Key component in Unit 4 steam generation cycle.",
        operating_parameters={
            "Max Pressure": "140 bar",
            "Normal Operating Temp": "65 °C - 80 °C",
            "Rated Speed": "2950 RPM",
            "Fluid Handled": "Deaerated Demineralized Water"
        },
        known_failure_modes=[
            "Mechanical seal flush breakdown (API Plan 53B)",
            "Drive-end roller bearing pitting due to lubricant contamination",
            "Cavitation during low suction tank T-301 level transients"
        ],
        historical_modifications=[
            "2023: Upgraded impeller material to Super Duplex Stainless Steel UNS S32750.",
            "2025: Installed high-frequency piezoelectric vibration sensors on drive and non-drive ends."
        ],
        ai_summary=f"Asset {asset_id} is a mission-critical rotating asset with high historical reliability but vulnerable to seal flush pressure drops. Continuous vibration monitoring recommended."
    )

@router.get("/incident-story/{incident_id}", response_model=IncidentStoryResponse)
def get_incident_story(incident_id: str):
    return IncidentStoryResponse(
        incident_id=incident_id,
        title="The Mystery of the Spiking Vibration: Pump P-101 Incident Narrative",
        narrative_story=(
            "On July 12th at 14:15, Unit 4 acoustic sensors registered a sudden frequency shift in Pump P-101. "
            "Lead Reliability Engineer Elena Rostova immediately initiated telemetry diagnostics. The AI Knowledge Graph "
            "linked the vibration anomaly to an identical event from March 2021, revealing that a sub-millimeter leak in seal flush line L-FEED-1004 "
            "was diluting the drive-end bearing oil. Thanks to cross-document reasoning, the maintenance crew replaced the seal cartridge in under 3 hours, avoiding a $280,000 un-planned outage."
        ),
        involved_engineers=["Elena Rostova", "Marcus Vance", "David K."],
        key_lessons=[
            "Seal flush differential pressure must be monitored via automated AI triggers.",
            "Always inspect nitrogen bladder pre-charge during quarterly PMs."
        ]
    )

@router.post("/agent-swarm")
def run_agent_swarm(payload: Dict[str, Any]):
    prompt = payload.get("prompt", "Analyze Pump P-101 failure risk and compliance status")
    target_asset = payload.get("target_asset", "P-101")
    return agent_swarm_service.execute_swarm_task(prompt, target_asset)

@router.get("/expert-preservation")
def get_expert_knowledge_preservation():
    return {
        "senior_engineer": "Dr. Aris Thorne (35 Years Plant Lead Architect)",
        "knowledge_nodes_extracted": 1420,
        "interviews_ingested": 18,
        "captured_heuristics": [
            "When Steam Valve V-101 sticks at 48%, check condensate drain valve D-402 first before replacing actuator.",
            "Pump P-101 cavitation noise at low flow is resolved by opening 2-inch recirculation line by 15%."
        ],
        "preservation_status": "Knowledge Graph Synchronized"
    }

@router.post("/memory")
def submit_industrial_memory(payload: IndustrialMemoryInput):
    kg_service.add_relationship(
        source=payload.asset_id.upper(),
        target=payload.engineer_name,
        rel_type="VERIFIED_BY_ENGINEER",
        attributes={"correction": payload.feedback_correction, "root_cause": payload.verified_root_cause}
    )
    return {
        "status": "Success",
        "message": f"Industrial Memory updated for {payload.asset_id} by Engineer {payload.engineer_name}. Knowledge Graph re-weighted.",
        "graph_node_updated": payload.asset_id.upper()
    }

@router.get("/cross-plant", response_model=List[CrossPlantComparison])
def get_cross_plant_intelligence():
    return [
        CrossPlantComparison(
            pattern_name="High Pressure Seal Flush Pressure Drop Anomaly",
            analyzed_plants=["Plant 1 (Houston, USA)", "Plant 2 (Rotterdam, NL)", "Plant 3 (Jamshedpur, IN)"],
            affected_asset_types=["Boiler Feed Pump P-101", "High Pressure Booster Pump P-402"],
            common_failure_mode="Nitrogen accumulator bladder pre-charge decay under high ambient summer temperatures.",
            recurring_frequency="Bi-annual seasonal pattern",
            recommended_global_action="Mandate automated nitrogen bladder pressure telemetry sensors across all global sites."
        )
    ]

@router.get("/plant-doctor", response_model=AIPlantDoctorBriefing)
def get_plant_doctor_briefing():
    return AIPlantDoctorBriefing(
        briefing_date="2026-07-20 22:40",
        overall_plant_status="Warning - 2 High Priority Action Items Pending",
        top_equipment_risks=[
            {"asset_id": "V-101", "risk": "Critical Red", "issue": "Actuator diaphragm friction overload", "rul_days": 6},
            {"asset_id": "P-101", "risk": "Orange Warning", "issue": "Bearing vibration 6.8 mm/s", "rul_days": 18}
        ],
        predicted_total_downtime_hours=18.5,
        active_compliance_issues=[
            {"standard": "OISD-137", "asset": "P-101", "detail": "Emergency closure response time delayed by 1.4s"}
        ],
        estimated_financial_loss_usd=280000.0,
        recommended_priority_actions=[
            "Dispatch instrument technician to perform Plan 53B re-charge on Pump P-101.",
            "Schedule 2-hour window on Valve V-101 for diaphragm packing inspection."
        ]
    )

@router.get("/executive-decision/{asset_id}", response_model=ExecutiveDecisionComparison)
def get_executive_decision(asset_id: str):
    a_id = asset_id.upper()
    options = [
        StrategyOption(
            strategy_name="Strategy A: Run to Failure",
            cost_usd=280000.0,
            downtime_hours=14.5,
            risk_level="Critical",
            estimated_savings_usd=0.0,
            is_recommended=False
        ),
        StrategyOption(
            strategy_name="Strategy B: Unplanned Complete Assembly Replacement",
            cost_usd=48000.0,
            downtime_hours=6.0,
            risk_level="Moderate",
            estimated_savings_usd=232000.0,
            is_recommended=False
        ),
        StrategyOption(
            strategy_name="Strategy C: Predictive Seal & Bearing Overhaul (Recommended)",
            cost_usd=4200.0,
            downtime_hours=2.0,
            risk_level="Minimal",
            estimated_savings_usd=275800.0,
            is_recommended=True
        )
    ]

    return ExecutiveDecisionComparison(
        asset_id=a_id,
        decision_title=f"Executive Action Comparison & Financial ROI Analysis for {a_id}",
        options=options,
        optimal_recommendation="Strategy C (Predictive Overhaul) maximizes plant uptime while delivering $275,800 in avoided outage losses."
    )
