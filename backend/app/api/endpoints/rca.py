from fastapi import APIRouter
from app.models.schemas import RCAResponse, FishboneCategory

router = APIRouter()

@router.get("/analyze/{asset_id}", response_model=RCAResponse)
def get_rca_analysis(asset_id: str):
    fishbone = [
        FishboneCategory(category="Machine", causes=["Drive-end bearing race pitting", "API Plan 53B pressure orifice wear"]),
        FishboneCategory(category="Method", causes=["Standard lubrication interval missed by 14 days", "Vibration baseline threshold uncalibrated"]),
        FishboneCategory(category="Material", causes=["Seal flush oil contamination (0.8% water content)", "Non-OEM gasket sealant used in 2025 overhaul"]),
        FishboneCategory(category="Manpower", causes=["Turnover in Unit 4 lead technician team", "Field shift handover log incomplete"]),
        FishboneCategory(category="Measurement", causes=["Analog pressure gauge drift (+0.6 bar error)", "SCADA telemetry sampling rate at 15m interval"]),
        FishboneCategory(category="Environment", causes=["High ambient summer temperature (44°C)", "Humidity in auxiliary pump enclosure"])
    ]

    five_whys = [
        {"why": "Why did Pump P-101 fail high vibration limit?", "answer": "The drive-end roller bearing developed micro-pitting on its inner race."},
        {"why": "Why did the bearing inner race pit?", "answer": "The lubricating oil lost film viscosity due to seal fluid dilution."},
        {"why": "Why was the oil diluted with seal fluid?", "answer": "The mechanical seal throttle bushing leaked pressure under transient loads."},
        {"why": "Why did the seal bushing leak?", "answer": "The flush plan accumulator pressure dropped below suction pressure."},
        {"why": "Why did accumulator pressure drop?", "answer": "Root Cause: Nitrogen bladder pre-charge was not checked during the Q2 preventive maintenance cycle."}
    ]

    timeline = [
        {"time": "08:15", "event": "Nitrogen accumulator pre-charge drops to 1.8 bar"},
        {"time": "11:30", "event": "Mechanical seal faces separate slightly under 120 bar discharge"},
        {"time": "14:00", "event": "Diluted oil enters drive-end bearing cavity"},
        {"time": "16:45", "event": "Vibration sensor records 6.8 mm/s peak RMS; AI triggers Warning Alert"}
    ]

    return RCAResponse(
        incident_title=f"Root Cause Analysis - Drive-End Bearing Anomaly on {asset_id}",
        asset_id=asset_id,
        fishbone=fishbone,
        five_whys=five_whys,
        timeline=timeline,
        recommended_fixes=["Re-charge nitrogen accumulator to 4.5 bar", "Flush bearing oil cavity with ISO VG 46 synthetic lubricant"],
        preventive_actions=["Enforce mandatory Q2 nitrogen bladder checks in Maintenance Management System (MMS)"]
    )
