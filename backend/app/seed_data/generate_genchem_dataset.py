import os
import json
import random
import csv
from datetime import datetime, timedelta

DATASET_DIR = os.path.join(os.path.dirname(__file__), "demo_dataset")

PLANT_AREAS = [
    "Pump House", "Boiler Section", "Utilities", "Cooling Tower", 
    "Compressor Area", "Tank Farm", "Process Area", "Control Room"
]

MANUFACTURERS = ["Flowserve", "Emerson Fisher", "Sulzer", "Siemens", "ABB", "KSB Pumps", "General Electric"]

def generate_assets():
    assets = []
    asset_types = ["Pump", "Valve", "Compressor", "Motor", "HeatExchanger", "Boiler", "Tank", "Pipeline", "FlowMeter", "PressureTransmitter"]
    
    for i in range(1, 121):
        atype = asset_types[i % len(asset_types)]
        prefix = atype[0].upper()
        if atype == "HeatExchanger": prefix = "HE"
        elif atype == "FlowMeter": prefix = "FM"
        elif atype == "PressureTransmitter": prefix = "PT"
        
        asset_id = f"{prefix}-{100 + i}"
        area = PLANT_AREAS[i % len(PLANT_AREAS)]
        mfg = MANUFACTURERS[i % len(MANUFACTURERS)]
        health = round(random.uniform(55.0, 99.0), 1)
        risk = "Red" if health < 60 else ("Orange" if health < 75 else "Green")
        rul = max(3, int((health / 100.0) * 120))

        assets.append({
            "asset_id": asset_id,
            "name": f"GenChem {atype} {asset_id}",
            "type": atype,
            "area": area,
            "manufacturer": mfg,
            "installation_date": f"201{random.randint(5,9)}-0{random.randint(1,9)}-15",
            "specifications": {
                "design_pressure_bar": random.choice([40, 90, 140]),
                "rated_temp_c": random.choice([60, 85, 120, 350]),
                "max_vibration_rms": 4.5
            },
            "connected_equipment": [f"V-{100 + ((i + 1) % 120 + 1)}", f"T-{100 + ((i + 2) % 120 + 1)}"],
            "health_score": health,
            "risk_score": risk,
            "remaining_useful_life_days": rul,
            "compliance_status": "Compliant" if health >= 70 else "Action Required"
        })
    return assets

def generate_documents():
    docs_dir = os.path.join(DATASET_DIR, "documents")
    os.makedirs(docs_dir, exist_ok=True)

    doc_list = []
    
    # 20 OEM Manuals
    for i in range(1, 21):
        fname = f"OEM_Manual_Pump_P{100+i}.txt"
        content = f"""GenChem Refinery OEM Manual: Pump P-{100+i}
Manufacturer: Flowserve | Model: High Pressure Centrifugal
Design Pressure: 140 bar | Rated Temperature: 85°C | Flow: 450 m3/h
Maintenance Standard: API Plan 53B Pressurized Flush System.
Continuous Vibration Threshold: 4.5 mm/s RMS.
Lube Oil Standard: ISO VG 46 Synthetic Fluid."""
        with open(os.path.join(docs_dir, fname), "w", encoding="utf-8") as f:
            f.write(content)
        doc_list.append({"doc_id": f"DOC-OEM-{i}", "filename": fname, "type": "OEM Manual"})

    # 30 Incident Reports
    for i in range(1, 31):
        fname = f"Incident_Report_INC_2026_{100+i}.txt"
        content = f"""GenChem Refinery Incident Report ID: INC-2026-{100+i}
Date: 2026-06-15 | Plant Area: Pump House
Target Asset: P-{100+i} | Lead Engineer: Elena Rostova
Failure Mode: Mechanical seal barrier fluid pressure drop causing drive-end bearing overheating.
Vibration Peak Recorded: 6.84 mm/s RMS.
Root Cause: Nitrogen bladder pre-charge pressure drop in Plan 53B accumulator.
Corrective Action: System re-pressurized to 4.5 bar, lube oil flushed."""
        with open(os.path.join(docs_dir, fname), "w", encoding="utf-8") as f:
            f.write(content)
        doc_list.append({"doc_id": f"DOC-INC-{i}", "filename": fname, "type": "Incident Report"})

    # 20 SOP Documents
    for i in range(1, 21):
        fname = f"SOP_Emergency_Isolation_Asset_P{100+i}.txt"
        content = f"""GenChem Refinery Standard Operating Procedure: SOP-ISO-{100+i}
Target Asset: P-{100+i} | Category: Emergency Maintenance & LOTO
PPE Required: Nitrile Gloves, Arc Flash Suit Cat 2, Steel Toe Boots, Safety Goggles.
Tools: Torque Wrench 200 Nm, Laser Alignment Kit, Nitrogen Charging Cart.
Steps:
1. Isolate 4160V feeder breaker for Motor M-{100+i}.
2. Depressurize suction line L-FEED-1004 to 0 bar.
3. Torque coupling bolts to 140 N-m.
4. Verify laser runout <0.02 mm before energizing."""
        with open(os.path.join(docs_dir, fname), "w", encoding="utf-8") as f:
            f.write(content)
        doc_list.append({"doc_id": f"DOC-SOP-{i}", "filename": fname, "type": "SOP"})

    return doc_list

def generate_telemetry_csv():
    csv_path = os.path.join(DATASET_DIR, "genchem_sensor_telemetry_3year.csv")
    headers = ["timestamp", "asset_id", "pressure_bar", "temperature_c", "flow_m3h", "rpm", "vibration_rms", "current_a", "oil_condition_index"]
    
    start_date = datetime(2023, 7, 20, 0, 0)
    
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        
        # Write representative historical sample rows
        for day in range(0, 30):
            current_time = start_date + timedelta(days=day)
            for asset_num in range(101, 115):
                asset_id = f"P-{asset_num}"
                vib = round(random.uniform(2.1, 3.8), 2) if day < 20 else round(random.uniform(5.8, 6.9), 2)
                temp = round(random.uniform(62.0, 74.0), 1) if day < 20 else round(random.uniform(78.0, 86.5), 1)
                press = round(random.uniform(115.0, 122.0), 1)
                flow = round(random.uniform(420.0, 455.0), 1)
                rpm = 2950
                amp = round(random.uniform(395.0, 412.0), 1)
                oil_idx = round(random.uniform(85.0, 98.0), 1) if day < 20 else round(random.uniform(42.0, 58.0), 1)

                writer.writerow([current_time.strftime("%Y-%m-%d %H:%M:%S"), asset_id, press, temp, flow, rpm, vib, amp, oil_idx])

def generate_knowledge_graph(assets):
    nodes = []
    edges = []
    
    for a in assets:
        nodes.append({"id": a["asset_id"], "label": a["name"], "type": a["type"], "attributes": {"area": a["area"], "health": a["health_score"]}})
    
    for i in range(len(assets) - 1):
        edges.append({"source": assets[i]["asset_id"], "target": assets[i+1]["asset_id"], "type": "CONNECTED_TO", "attributes": {"line": "High Pressure Fluid Header"}})
        if i % 3 == 0:
            edges.append({"source": assets[i]["asset_id"], "target": "DOC-OEM-1", "type": "DOCUMENTED_IN", "attributes": {"section": "Manual"}})
    
    return {"nodes": nodes, "edges": edges}

def generate_incident_storylines():
    storylines = []
    for i in range(1, 21):
        storylines.append({
            "scenario_id": f"SCENARIO-2026-{100+i}",
            "title": f"GenChem High Pressure Pump P-{100+i} Bearing Pitting Event",
            "trigger_asset": f"P-{100+i}",
            "sensor_anomaly": "Vibration RMS spiked from 2.8 mm/s to 6.84 mm/s over 48 hours.",
            "maintenance_finding": "API Plan 53B nitrogen accumulator bladder pressure decay to 1.8 bar.",
            "inspection_report": "Drive-end bearing race micro-pitting caused by seal fluid lube oil dilution.",
            "lessons_learned": "Install continuous wireless pressure telemetry on Plan 53B accumulator bladders.",
            "compliance_impact": "OISD-137 maintenance response time non-conformance flag.",
            "executive_decision": "Execute Predictive Seal Overhaul ($4,200) vs Run-to-Failure ($280,000 loss)."
        })
    return storylines

def generate_demo_questions():
    questions = []
    topics = ["Why did Pump P-101 fail?", "What is the remaining useful life of Valve V-101?", "Generate emergency LOTO SOP for Pump P-101", "Show 2-hop Knowledge Graph connections for P-101", "Compare maintenance strategies for GenChem Boiler Feed System"]
    
    for i in range(1, 101):
        questions.append({
            "question_id": f"Q-{i:03d}",
            "text": f"{topics[i % len(topics)]} (Query Variant #{i})",
            "category": "Diagnostic" if i % 2 == 0 else "Predictive"
        })
    return questions

def generate_judge_demo_script():
    script_path = os.path.join(DATASET_DIR, "JUDGE_DEMO_SCRIPT.md")
    content = """# GenChem Refinery: Complete Hackathon Demonstration Script

## Step 1: Executive Command Center & Risk Heatmap
- **Action**: Open main dashboard (`/`).
- **Narrative**: "Welcome to GenChem Refinery's AI Operating System, INDUSTRIAL BRAIN. The live risk heatmap indicates Unit 4 Boiler Bay is operating under Warning State due to Pump P-101."

## Step 2: Multi-Hop Knowledge Graph Explorer & Time Travel
- **Action**: Navigate to `/graph` and drag the Time Travel slider from 2021 to 2026.
- **Narrative**: "Watch how the Knowledge Graph reconstructs plant evolution from initial 2021 commissioning to 2026 high-vibration incident linkages."

## Step 3: Industrial RAG Copilot with Trust Score & Citations
- **Action**: Open `/copilot` and submit query: *"Why did Pump P-101 fail vibration test?"*
- **Narrative**: "INDUSTRIAL BRAIN fuses dense vector search, sparse keyword matching, and graph traversal. It delivers a 94.8% Trust Score backed by exact page citations from OEM Manuals and Incident Reports."

## Step 4: 8-Agent Autonomous Swarm Collaboration Trace
- **Action**: Open `/innovations` and launch Swarm Task *"Audit Pump P-101"*.
- **Narrative**: "Observe 8 autonomous agents (Knowledge, Maintenance, Compliance, RCA, Audit, Graph, Doc, Coordinator) collaborating in real time."

## Step 5: Equipment DNA & AI Plant Doctor Executive Briefing
- **Action**: Open `/digital-twin` and inspect `Equipment DNA: DNA-HYD-99841-P101`.
- **Narrative**: "Every asset possesses a persistent Equipment DNA profile tracking lifetime maintenance, failure history, and compliance metrics."

## Step 6: Executive Decision Strategy Engine
- **Action**: View Executive Decision Comparison for `P-101`.
- **Narrative**: "The AI compares Run to Failure ($280k loss) vs Predictive Overhaul ($4.2k cost), recommending the optimal strategy with $275,800 net savings."
"""
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(content)

def build_genchem_dataset():
    os.makedirs(DATASET_DIR, exist_ok=True)
    
    assets = generate_assets()
    with open(os.path.join(DATASET_DIR, "genchem_assets.json"), "w", encoding="utf-8") as f:
        json.dump(assets, f, indent=2)

    docs = generate_documents()
    with open(os.path.join(DATASET_DIR, "genchem_documents_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(docs, f, indent=2)

    generate_telemetry_csv()

    kg = generate_knowledge_graph(assets)
    with open(os.path.join(DATASET_DIR, "genchem_knowledge_graph.json"), "w", encoding="utf-8") as f:
        json.dump(kg, f, indent=2)

    storylines = generate_incident_storylines()
    with open(os.path.join(DATASET_DIR, "genchem_incident_storylines.json"), "w", encoding="utf-8") as f:
        json.dump(storylines, f, indent=2)

    questions = generate_demo_questions()
    with open(os.path.join(DATASET_DIR, "genchem_demo_questions.json"), "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2)

    generate_judge_demo_script()

    return f"GenChem Refinery Demo Dataset successfully created at {DATASET_DIR}"

if __name__ == "__main__":
    print(build_genchem_dataset())
