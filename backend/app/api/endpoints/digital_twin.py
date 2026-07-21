from fastapi import APIRouter
from app.models.schemas import DigitalTwinDetail, EquipmentChatQuery, EquipmentDNA
from app.seed_data.seed_data import SAMPLE_ASSETS

router = APIRouter()

@router.get("/{asset_id}", response_model=DigitalTwinDetail)
def get_digital_twin(asset_id: str):
    a_id = asset_id.upper()
    for asset in SAMPLE_ASSETS:
        if asset["id"].upper() == a_id:
            return DigitalTwinDetail(
                asset_id=asset["id"],
                name=asset["name"],
                type=asset["type"],
                location=asset["location"],
                status=asset["status"],
                specifications=asset["specifications"],
                telemetry=asset["telemetry"],
                connected_assets=asset["connected_assets"],
                active_risk_score=asset["failure_probability"] * 100,
                documents=asset["documents"],
                recent_maintenance=asset["recent_maintenance"]
            )
    raise HTTPException(status_code=404, detail=f"Asset {asset_id} digital twin not found.")

@router.post("/chat")
def chat_with_equipment(payload: EquipmentChatQuery):
    a_id = payload.asset_id.upper()
    msg = payload.message.lower()
    
    if "health" in msg or "status" in msg or "how are you" in msg:
        reply = f"Hello! I am {a_id}. My current health score is 64.5%. My drive-end bearing is running at 78.4°C and vibration is at 6.8 mm/s. I need a mechanical seal flush check!"
    elif "maint" in msg or "repair" in msg:
        reply = f"My last maintenance was on 2026-05-10 by Eng. Elena Rostova for Mechanical Seal Replacement. My next planned check is in 6 days."
    else:
        reply = f"Regarding '{payload.message}': As {a_id}, my operating pressure is 118 bar. All telemetry parameters are being streamed to the INDUSTRIAL BRAIN graph engine."

    return {
        "asset_id": payload.asset_id,
        "reply": reply,
        "confidence": 0.96
    }

@router.get("/dna/{asset_id}", response_model=EquipmentDNA)
def get_equipment_dna(asset_id: str):
    a_id = asset_id.upper()
    return EquipmentDNA(
        asset_id=a_id,
        name=f"Boiler Feed Equipment {a_id}",
        category="Rotating High-Pressure Machinery",
        dna_fingerprint="DNA-HYD-99841-P101-REV4",
        composite_health_index=64.5,
        installation_date="2021-03-15",
        timeline=[
            {"date": "2021-03-15", "event": "Initial Plant Commissioning & Alignment"},
            {"date": "2023-08-10", "event": "Super Duplex Impeller Upgrade"},
            {"date": "2026-05-10", "event": "Mechanical Seal Cartridge Replacement"},
            {"date": "2026-07-12", "event": "Vibration Anomaly Event (6.8 mm/s Peak)"}
        ],
        maintenance_history=[
            {"date": "2026-05-10", "action": "Seal Replacement", "cost_usd": 4200, "engineer": "Elena Rostova"},
            {"date": "2025-11-20", "action": "Bearing Lubrication", "cost_usd": 1100, "engineer": "Marcus Vance"}
        ],
        failure_history=[
            {"date": "2026-07-12", "failure_mode": "Drive-End Bearing Race Pitting", "severity": "High"}
        ],
        compliance_history=[
            {"standard": "ISO 55001", "status": "Compliant"},
            {"standard": "OISD-137", "status": "Action Required (Delay 1.4s)"}
        ],
        ai_summary=f"Persistent Equipment DNA profile for {a_id}: High operational reliability with known vulnerability to API Plan 53B nitrogen bladder pressure drops."
    )
