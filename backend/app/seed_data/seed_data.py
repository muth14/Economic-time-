from typing import Dict, Any, List

SAMPLE_ASSETS = [
    {
        "id": "P-101",
        "name": "Centrifugal Boiler Feed Pump P-101",
        "type": "Pump",
        "category": "Rotating Equipment",
        "location": "Unit 4 - Power & Utility Bay",
        "status": "Warning",
        "health_score": 64.5,
        "rul_days": 18,
        "failure_probability": 0.35,
        "risk_level": "Orange",
        "specifications": {
            "Flow Rate": "450 m³/h",
            "Head Pressure": "120 bar",
            "Motor Power": "350 kW",
            "Manufacturer": "Flowserve Corp",
            "Serial Number": "FS-2021-99841",
            "Installation Date": "2021-03-15"
        },
        "telemetry": {
            "Vibration (RMS)": "6.8 mm/s (High)",
            "Bearing Temp DE": "78.4 °C",
            "Suction Pressure": "4.2 bar",
            "Discharge Pressure": "118 bar",
            "Motor Amperage": "410 A"
        },
        "connected_assets": ["V-101", "T-301", "M-102", "C-201"],
        "recent_maintenance": [
            {"date": "2026-05-10", "type": "Mechanical Seal Replacement", "engineer": "Elena Rostova", "cost_usd": 4200},
            {"date": "2025-11-20", "type": "Bearing Lubrication & Realignment", "engineer": "Marcus Vance", "cost_usd": 1100}
        ],
        "documents": [
            {"id": "DOC-101", "name": "Pump_P101_OEM_Manual.pdf", "type": "OEM Manual"},
            {"id": "DOC-102", "name": "P101_Vibration_Anomaly_Incident_Report.pdf", "type": "Incident Report"},
            {"id": "DOC-103", "name": "P_AND_ID_Boiler_Feed_System_Rev4.pdf", "type": "P&ID Schematic"}
        ]
    },
    {
        "id": "V-101",
        "name": "Main Steam Pressure Control Valve V-101",
        "type": "Valve",
        "category": "Flow Control",
        "location": "Unit 4 - Steam Header Line 2",
        "status": "Critical",
        "health_score": 42.0,
        "rul_days": 6,
        "failure_probability": 0.78,
        "risk_level": "Red",
        "specifications": {
            "Valve Size": "12 Inch",
            "Rating": "ANSI Class 900",
            "Actuator": "Pneumatic Diaphragm",
            "Manufacturer": "Fisher Emerson",
            "Serial Number": "FE-VALVE-7741"
        },
        "telemetry": {
            "Position Feedback": "48% (Target: 60%)",
            "Actuator Air Pressure": "3.1 bar",
            "Upstream Pressure": "88 bar",
            "Stem Friction Index": "Elevated"
        },
        "connected_assets": ["P-101", "T-301"],
        "recent_maintenance": [
            {"date": "2026-02-14", "type": "Actuator Packing Inspection", "engineer": "David K.", "cost_usd": 850}
        ],
        "documents": [
            {"id": "DOC-104", "name": "Valve_V101_Calibration_Certificate.pdf", "type": "Quality Document"}
        ]
    },
    {
        "id": "C-201",
        "name": "Heavy Duty Hydrogen Gas Compressor C-201",
        "type": "Compressor",
        "category": "Rotating Equipment",
        "location": "Hydrocracker Unit B",
        "status": "Normal",
        "health_score": 92.0,
        "rul_days": 145,
        "failure_probability": 0.05,
        "risk_level": "Green",
        "specifications": {
            "Capacity": "12,000 Nm³/h",
            "Compression Stages": "3 Stage Reciprocating",
            "Motor Driver": "6kV Synchronous 1.2MW",
            "Manufacturer": "Siemens Energy"
        },
        "telemetry": {
            "Suction Temp": "34 °C",
            "Discharge Temp Stage 3": "142 °C",
            "Lube Oil Pressure": "5.4 bar",
            "RPM": "1480"
        },
        "connected_assets": ["P-101"],
        "recent_maintenance": [
            {"date": "2026-01-05", "type": "Annual Major Overhaul", "engineer": "Siemens Field Crew", "cost_usd": 48000}
        ],
        "documents": [
            {"id": "DOC-105", "name": "Compressor_C201_Major_Overhaul_Report.pdf", "type": "Maintenance Report"}
        ]
    },
    {
        "id": "T-301",
        "name": "High-Pressure Feedwater Storage Tank T-301",
        "type": "Tank",
        "category": "Static Equipment",
        "location": "Utilities Tank Farm South",
        "status": "Normal",
        "health_score": 88.0,
        "rul_days": 320,
        "failure_probability": 0.08,
        "risk_level": "Green",
        "specifications": {
            "Capacity": "500 m³",
            "Design Pressure": "15 bar",
            "Shell Thickness": "24 mm",
            "Material": "SA-516 Gr 70 Steel"
        },
        "telemetry": {
            "Liquid Level": "74.2 %",
            "Internal Temp": "85 °C",
            "Vapor Pressure": "2.8 bar"
        },
        "connected_assets": ["P-101", "V-101"],
        "recent_maintenance": [
            {"date": "2025-08-12", "type": "Ultrasonic Thickness Test", "engineer": "TUV Rheinland Inspector", "cost_usd": 3200}
        ],
        "documents": [
            {"id": "DOC-106", "name": "Tank_T301_UT_Thickness_Inspection.pdf", "type": "Inspection Report"}
        ]
    },
    {
        "id": "M-102",
        "name": "High Voltage Electric Drive Motor M-102",
        "type": "Motor",
        "category": "Electrical Drive",
        "location": "Unit 4 - Power & Utility Bay",
        "status": "Warning",
        "health_score": 71.0,
        "rul_days": 42,
        "failure_probability": 0.22,
        "risk_level": "Yellow",
        "specifications": {
            "Power Rating": "350 kW",
            "Voltage": "4160 V",
            "Current": "62 A",
            "Speed": "2980 RPM"
        },
        "telemetry": {
            "Stator Temp Phase A": "98.2 °C (Elevated)",
            "Winding Insulation Index": "Acceptable",
            "Current Unbalance": "2.1 %"
        },
        "connected_assets": ["P-101"],
        "recent_maintenance": [
            {"date": "2026-04-02", "type": "Megger Winding Resistance Test", "engineer": "Alex Chen", "cost_usd": 900}
        ],
        "documents": [
            {"id": "DOC-107", "name": "Motor_M102_Thermography_Analysis.pdf", "type": "Inspection Report"}
        ]
    }
]

SAMPLE_DOCUMENTS = [
    {
        "id": "DOC-101",
        "filename": "Pump_P101_OEM_Manual.pdf",
        "file_type": "PDF",
        "upload_time": "2026-06-01 10:30:00",
        "status": "Indexed",
        "page_count": 48,
        "risk_level": "Low",
        "summary": "Official Flowserve OEM Operating Manual for Boiler Feed Pump P-101 detailing vibration thresholds, seal flush plans (API Plan 53B), bearing temperature limits (<85°C), and preventive maintenance intervals.",
        "entities": [
            {"category": "Equipment", "value": "P-101", "confidence": 0.99},
            {"category": "Temperature Limit", "value": "85 °C", "confidence": 0.95},
            {"category": "Pressure Limit", "value": "140 bar", "confidence": 0.94},
            {"category": "Vendor", "value": "Flowserve Corp", "confidence": 0.98},
            {"category": "Vibration Limit", "value": "4.5 mm/s RMS", "confidence": 0.92}
        ]
    },
    {
        "id": "DOC-102",
        "filename": "P101_Vibration_Anomaly_Incident_Report.pdf",
        "file_type": "PDF",
        "upload_time": "2026-07-12 14:15:00",
        "status": "Indexed",
        "page_count": 6,
        "risk_level": "High",
        "summary": "Root cause investigation into P-101 high drive-end bearing vibration (6.8 mm/s). The failure was attributed to mechanical seal leakage flushing lube oil out of the housing, resulting in micro-pitting on roller race.",
        "entities": [
            {"category": "Equipment", "value": "P-101", "confidence": 0.99},
            {"category": "Failure Code", "value": "FAIL-BRG-2201", "confidence": 0.96},
            {"category": "Engineer", "value": "Elena Rostova", "confidence": 0.97},
            {"category": "Maintenance Action", "value": "Seal Replacement & Race Polishing", "confidence": 0.93},
            {"category": "Root Cause", "value": "Lube Oil Dilution via Seal Leak", "confidence": 0.95}
        ]
    },
    {
        "id": "DOC-103",
        "filename": "P_AND_ID_Boiler_Feed_System_Rev4.pdf",
        "file_type": "P&ID Schematic",
        "upload_time": "2026-07-01 09:00:00",
        "status": "Indexed",
        "page_count": 1,
        "risk_level": "Medium",
        "summary": "Piping & Instrumentation Diagram showing high-pressure boiler feed loop connecting Tank T-301 through Pump P-101 to Control Valve V-101 and Motor M-102 drive train.",
        "entities": [
            {"category": "Equipment Tag", "value": "P-101", "confidence": 0.99},
            {"category": "Equipment Tag", "value": "V-101", "confidence": 0.99},
            {"category": "Equipment Tag", "value": "T-301", "confidence": 0.99},
            {"category": "Line Tag", "value": "L-FEED-1004-900#", "confidence": 0.91}
        ]
    }
]

SAMPLE_KNOWLEDGE_GRAPH = {
    "nodes": [
        {"id": "P-101", "label": "P-101 Boiler Feed Pump", "type": "Pump", "attributes": {"health": 64.5, "status": "Warning"}},
        {"id": "V-101", "label": "V-101 Steam Control Valve", "type": "Valve", "attributes": {"health": 42.0, "status": "Critical"}},
        {"id": "C-201", "label": "C-201 Hydrogen Compressor", "type": "Compressor", "attributes": {"health": 92.0, "status": "Normal"}},
        {"id": "T-301", "label": "T-301 Storage Tank", "type": "Tank", "attributes": {"health": 88.0, "status": "Normal"}},
        {"id": "M-102", "label": "M-102 Electric Motor", "type": "Motor", "attributes": {"health": 71.0, "status": "Warning"}},
        {"id": "ENG-01", "label": "Elena Rostova (Lead Reliability Eng)", "type": "Engineer", "attributes": {"dept": "Maintenance"}},
        {"id": "VEND-01", "label": "Flowserve Corp", "type": "Vendor", "attributes": {"country": "USA"}},
        {"id": "DOC-101", "label": "Pump_P101_OEM_Manual.pdf", "type": "Manual", "attributes": {"pages": 48}},
        {"id": "DOC-102", "label": "P101_Vibration_Anomaly.pdf", "type": "Incident", "attributes": {"date": "2026-07-12"}},
        {"id": "SOP-12", "label": "High Pressure Flush SOP-12", "type": "SafetyProcedure", "attributes": {"rev": 3}},
        {"id": "REG-ISO", "label": "ISO 55001 Asset Standard", "type": "Regulation", "attributes": {"category": "Compliance"}}
    ],
    "edges": [
        {"source": "M-102", "target": "P-101", "type": "CONNECTED_TO", "attributes": {"coupling": "Flexible Gear"}},
        {"source": "P-101", "target": "V-101", "type": "CONNECTED_TO", "attributes": {"fluid": "High Temp Water"}},
        {"source": "T-301", "target": "P-101", "type": "CONNECTED_TO", "attributes": {"line": "Suction Line 14-Inch"}},
        {"source": "P-101", "target": "DOC-102", "type": "FAILED_DUE_TO", "attributes": {"reason": "Seal Flush Degradation"}},
        {"source": "P-101", "target": "ENG-01", "type": "MAINTAINED_BY", "attributes": {"frequency": "Bi-weekly"}},
        {"source": "P-101", "target": "VEND-01", "type": "USES", "attributes": {"part": "Mechanical Seal Assembly"}},
        {"source": "DOC-101", "target": "P-101", "type": "REFERENCES", "attributes": {"relevance": 1.0}},
        {"source": "P-101", "target": "SOP-12", "type": "USES", "attributes": {"mandatory": True}},
        {"source": "P-101", "target": "REG-ISO", "type": "REFERENCES", "attributes": {"section": "Clause 8.1"}}
    ]
}
