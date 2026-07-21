import os
import json
import csv
import random
from datetime import datetime, timedelta

MASTER_DIR = os.path.join(os.path.dirname(__file__), "demo_dataset")

SUBDIRS = [
    "assets", "documents", "pid", "telemetry", "maintenance", 
    "inspection", "incidents", "audits", "emails", "vendors", 
    "permits", "sops", "knowledge_graph", "equipment_dna", 
    "executive", "questions", "demo_script"
]

ENGINEERS = [
    {"name": "Dr. Heinrich Weber", "role": "Plant Manager"},
    {"name": "Elena Rostova", "role": "Lead Reliability Engineer"},
    {"name": "Marcus Vance", "role": "Senior Maintenance Engineer"},
    {"name": "Ananya Sharma", "role": "Control Room Operator"},
    {"name": "Vikram Malhotra", "role": "Safety & LOTO Officer"},
    {"name": "Auditor Thomas Sterling", "role": "ISO 55001 Compliance Auditor"}
]

PLANTS = ["GenChem Refinery Main (Jamshedpur)", "GenChem Plant Houston (USA)", "GenChem Plant Rotterdam (NL)"]

def create_directory_structure():
    for sd in SUBDIRS:
        os.makedirs(os.path.join(MASTER_DIR, sd), exist_ok=True)

def generate_master_assets():
    filepath = os.path.join(MASTER_DIR, "assets", "genchem_assets_master.json")
    if os.path.exists(filepath):
        return
    
    assets = []
    types = ["Pump", "Valve", "Compressor", "Motor", "HeatExchanger", "Boiler", "Tank", "Pipeline", "PressureTransmitter", "FlowMeter", "TemperatureSensor", "ControlValve", "SafetyValve"]
    areas = ["Pump House", "Boiler Section", "Utilities", "Cooling Tower", "Compressor Area", "Tank Farm", "Process Area", "Control Room"]
    mfgs = ["Flowserve", "Emerson Fisher", "Sulzer", "Siemens", "ABB", "KSB Pumps", "General Electric"]

    for i in range(1, 131):
        atype = types[i % len(types)]
        prefix = atype[0].upper()
        if atype == "HeatExchanger": prefix = "HE"
        elif atype == "FlowMeter": prefix = "FM"
        elif atype == "PressureTransmitter": prefix = "PT"
        elif atype == "ControlValve": prefix = "CV"
        elif atype == "SafetyValve": prefix = "SV"

        asset_id = f"{prefix}-{100 + i}"
        area = areas[i % len(areas)]
        mfg = mfgs[i % len(mfgs)]
        health = 64.5 if asset_id == "P-101" else (48.2 if asset_id == "V-102" else round(random.uniform(70.0, 99.0), 1))
        risk = "Critical Red" if health < 50 else ("Orange Warning" if health < 70 else "Green Normal")
        rul = 18 if asset_id == "P-101" else (6 if asset_id == "V-102" else max(12, int((health / 100.0) * 150)))

        assets.append({
            "asset_id": asset_id,
            "equipment_name": f"GenChem {atype} {asset_id}",
            "plant_area": area,
            "manufacturer": mfg,
            "model": f"Model-{mfg[:3].upper()}-99{i}",
            "serial_number": f"SN-2021-{88000+i}",
            "installation_date": "2021-03-15",
            "commissioning_date": "2021-04-01",
            "specifications": {
                "design_pressure_bar": 140 if "Pump" in atype or "Valve" in atype else 45,
                "rated_temp_c": 85 if "Pump" in atype else 350,
                "max_allowable_vibration_rms": 4.5
            },
            "operating_envelope": {
                "normal_pressure_range": "110-125 bar",
                "normal_temp_range": "65-78 °C",
                "normal_vibration_range": "1.5-3.5 mm/s"
            },
            "connected_equipment": [f"V-{100 + ((i + 1) % 130 + 1)}", f"T-{100 + ((i + 2) % 130 + 1)}"],
            "maintenance_history_count": 8,
            "failure_history_count": 2,
            "health_score": health,
            "risk_score": risk,
            "remaining_useful_life_days": rul,
            "compliance_status": "Action Required (OISD-137)" if health < 70 else "Compliant (ISO 55001)",
            "equipment_dna_id": f"DNA-GENCHEM-{asset_id}",
            "ai_summary": f"Master Equipment DNA for {asset_id}: Installed 2021. Primary failure mode is bearing race pitting linked to mechanical seal barrier pressure drops."
        })

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(assets, f, indent=2)

def generate_master_telemetry():
    filepath = os.path.join(MASTER_DIR, "telemetry", "genchem_3year_hourly_sensor_telemetry.csv")
    if os.path.exists(filepath):
        return

    headers = ["timestamp", "asset_id", "pressure_bar", "temperature_c", "flow_m3h", "rpm", "current_a", "voltage_v", "vibration_rms", "bearing_temp_de", "oil_condition_index", "motor_load_pct"]
    start_date = datetime(2023, 7, 20, 0, 0)

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        for hour in range(0, 100):
            current_time = start_date + timedelta(hours=hour)
            for asset_id in ["P-101", "V-102", "C-103", "T-104", "M-105"]:
                if asset_id == "P-101":
                    # Degradation pattern
                    vib = round(3.2 + (hour / 100.0) * 3.6, 2)  # Rises to 6.8 mm/s
                    temp = round(68.0 + (hour / 100.0) * 10.4, 1)  # Rises to 78.4 °C
                    oil_cond = round(95.0 - (hour / 100.0) * 45.0, 1)  # Drops to 50.0
                elif asset_id == "V-102":
                    vib = round(2.1 + (hour / 100.0) * 1.5, 2)
                    temp = round(72.0 + (hour / 100.0) * 18.0, 1)
                    oil_cond = 88.0
                else:
                    vib = round(random.uniform(1.8, 3.2), 2)
                    temp = round(random.uniform(60.0, 72.0), 1)
                    oil_cond = round(random.uniform(88.0, 98.0), 1)

                writer.writerow([
                    current_time.strftime("%Y-%m-%d %H:%M:%S"),
                    asset_id,
                    round(118.0 + random.uniform(-2.0, 2.0), 1),
                    temp,
                    round(445.0 + random.uniform(-10.0, 10.0), 1),
                    2950,
                    408,
                    4160,
                    vib,
                    temp + 2.5,
                    oil_cond,
                    round(84.5 + random.uniform(-3.0, 3.0), 1)
                ])

def generate_master_storyline_and_script():
    filepath_inc = os.path.join(MASTER_DIR, "incidents", "GENCHEM_MASTER_INCIDENT_STORYLINE.json")
    if not os.path.exists(filepath_inc):
        story = {
            "title": "GenChem Master Incident Story: Pump P-101 Bearing Degradation & Cascade Boiler Trip",
            "facility": "GenChem Refinery Main (Jamshedpur)",
            "timeline": [
                {"step": 1, "asset": "P-101", "event": "API Plan 53B accumulator nitrogen bladder pre-charge decayed to 1.8 bar."},
                {"step": 2, "asset": "P-101", "event": "Vibration RMS increased from 2.8 mm/s to 6.84 mm/s over 48 hours."},
                {"step": 3, "asset": "P-101", "event": "Drive-end bearing race micro-pitting observed by Operator Ananya Sharma."},
                {"step": 4, "asset": "V-102", "event": "Control Valve V-102 experienced partial actuator diaphragm packing blockage at 48% stroke."},
                {"step": 5, "asset": "HE-106", "event": "Hydraulic pressure surge propagated to Boiler Feed Header, causing Boiler B-201 high pressure trip."},
                {"step": 6, "asset": "PLANT", "event": "Emergency Plant Shutdown executed under LOTO SOP-12."},
                {"step": 7, "asset": "AUDIT", "event": "ISO 55001 & OISD-137 audit finding flagged 12-day maintenance delay."},
                {"step": 8, "asset": "RECOVERY", "event": "INDUSTRIAL BRAIN Multi-Agent Swarm generated Predictive Overhaul Plan ($4,200 cost vs $280,000 outage loss)."}
            ]
        }
        with open(filepath_inc, "w", encoding="utf-8") as f:
            json.dump(story, f, indent=2)

    filepath_script = os.path.join(MASTER_DIR, "demo_script", "16_STEP_MASTER_JUDGE_DEMO_GUIDE.md")
    if not os.path.exists(filepath_script):
        guide = """# GenChem Refinery: 16-Step Master Judge Demo Guide

1. **Upload OEM Manual** -> Ingest `documents/Pump_P101_OEM_Manual.txt`.
2. **OCR & Layout Engine** -> Extract Bounding Boxes & P&ID symbols.
3. **Entity Extraction** -> Extract `P-101`, `140 bar`, `4.5 mm/s limit`.
4. **Knowledge Graph Creation** -> Create nodes and `CONNECTED_TO` relationships.
5. **Equipment DNA Generation** -> Display `DNA-GENCHEM-P-101` persistent profile.
6. **Hybrid Retrieval** -> Combine dense vector + sparse BM25 + graph hop.
7. **AI Copilot Query** -> *"Why did Pump P-101 fail vibration test?"*
8. **Multi-Agent Swarm Debate** -> 8 Agents debate root cause & work orders.
9. **Explainability Dashboard** -> Show 94.8% Trust Score, citations, graph path.
10. **Failure Prediction** -> Weibull survival curve & 18 days RUL.
11. **Compliance Analysis** -> Audit OISD-137 & ISO 55001 gap report.
12. **Incident Replay** -> Replay 48-hour vibration degradation timeline.
13. **Digital Twin Telemetry** -> Stream live 6.8 mm/s vibration telemetry via WebSockets.
14. **Executive Decision Engine** -> Compare Strategy A ($280k loss) vs Strategy C ($4.2k overhaul).
15. **AI Plant Doctor Briefing** -> Daily executive risk briefing.
16. **Executive Dashboard Summary** -> Plant-wide health heatmap & ROI metrics.
"""
        with open(filepath_script, "w", encoding="utf-8") as f:
            f.write(guide)

def run_master_generator():
    create_directory_structure()
    generate_master_assets()
    generate_master_telemetry()
    generate_master_storyline_and_script()
    return f"GenChem Enterprise Master Dataset successfully built across 17 subfolders in {MASTER_DIR}"

if __name__ == "__main__":
    print(run_master_generator())
