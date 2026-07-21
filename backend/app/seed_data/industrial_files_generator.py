import os

DEMO_FILES_DIR = os.path.join(os.path.dirname(__file__), "demo_files")

FILES_CONTENT = {
    "Pump_P101_OEM_Manual.txt": """Flowserve OEM Boiler Feed Pump P-101 Manual
Serial Number: FS-2021-99841 | Model: 3-Stage High Pressure Centrifugal
Design Pressure: 140 bar | Rated Flow: 450 m3/h | Max Temperature: 85°C
Maintenance Periodicity: Quarterly Lubrication, Annual Coupling Alignment.
API Plan 53B Pressurized Barrier Fluid Flush System required for mechanical seal.
Continuous allowable RMS vibration limit: 4.5 mm/s.""",

    "P101_Vibration_Anomaly_Incident_Report.txt": """INCIDENT REPORT: P-101 High Vibration Anomaly
Date: 2026-07-12 | Unit: Power & Utility Bay 4
Lead Reliability Engineer: Elena Rostova | Incident ID: INC-2026-881
Root Cause: Mechanical seal flush nitrogen bladder pre-charge dropped to 1.8 bar, diluting drive-end bearing lube oil.
Vibration Peak: 6.8 mm/s RMS (OEM threshold: 4.5 mm/s).
Action Taken: API Plan 53B accumulator re-pressurized, oil cavity flushed with ISO VG 46 synthetic lubricant.""",

    "P_AND_ID_Boiler_Feed_System_Rev4.txt": """PIPING AND INSTRUMENTATION DIAGRAM (P&ID) - REV 4
System: High Pressure Boiler Feedwater Loop
Line Tag: L-FEED-1004-900#
Topological Flow: Feedwater Tank T-301 -> Suction Line 14-Inch -> Boiler Feed Pump P-101 -> Steam Header Valve V-101 -> High Pressure Main Boiler Header.
Motor Driver Tag: M-102 (350kW 4160V Drive Motor).""",

    "V101_Calibration_Certificate.txt": """QUALITY CALIBRATION CERTIFICATE - VALVE V-101
Manufacturer: Fisher Emerson | Size: 12 Inch ANSI 900#
Actuator Type: Pneumatic Diaphragm | Calibration Date: 2026-02-14
Stem Friction Index: 12% (Baseline) | Response Time: 1.2 Seconds
Certification Standard: ISO 9001 / ASME B16.34.""",

    "P101_Telemetry_Log.csv": """timestamp,asset_id,vibration_rms,bearing_temp_de,discharge_pressure_bar,motor_amperage_a
2026-07-20 21:00:00,P-101,6.72,78.1,118.2,408
2026-07-20 21:15:00,P-101,6.81,78.4,118.0,410
2026-07-20 21:30:00,P-101,6.79,78.3,118.5,409
2026-07-20 21:45:00,P-101,6.84,78.6,117.9,411""",

    "ISO_55001_Audit_Report.txt": """ISO 55001 ASSET MANAGEMENT COMPLIANCE AUDIT
Audit ID: AUD-2026-Q3 | Auditor: TUV Rheinland Certified Team
Overall Plant Compliance Score: 87.5%
Findings:
1. P-101 Mechanical Seal Flush PM overdue by 12 days under OISD-137.
2. Tank T-301 safety relief valve re-certification due in 14 days under PESO.""",

    "Emergency_Seal_Flush_SOP.txt": """STANDARD OPERATING PROCEDURE: EMERGENCY SEAL FLUSH
Procedure ID: SOP-12-FLUSH | Asset: P-101
Tools: API Plan 53B Flush Cart, Torque Wrench 200 Nm, Nitrogen Cylinder.
PPE: Nitrile Gloves, Safety Goggles, Steel Toe Boots, Arc Flash Suit Cat 2.
Steps:
1. Lock Out Tag Out (LOTO) 4160V feeder breaker for Motor M-102.
2. Depressurize suction line L-FEED-1004 to 0 bar.
3. Re-charge nitrogen accumulator to 4.5 bar using Plan 53B cart.
4. Verify laser alignment runout <0.02 mm."""
}

def generate_industrial_demo_dataset():
    os.makedirs(DEMO_FILES_DIR, exist_ok=True)
    for filename, content in FILES_CONTENT.items():
        filepath = os.path.join(DEMO_FILES_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    return f"Successfully generated {len(FILES_CONTENT)} industrial demo files in {DEMO_FILES_DIR}"

if __name__ == "__main__":
    print(generate_industrial_demo_dataset())
