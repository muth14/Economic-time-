from fastapi import APIRouter
from app.models.schemas import ComplianceReport

router = APIRouter()

@router.get("/report", response_model=ComplianceReport)
def get_compliance_report():
    return ComplianceReport(
        report_id="COMP-2026-Q3-009",
        standard="ISO 55001 Asset Management & OISD-137 Fire & Safety Standard",
        compliance_score=87.5,
        violations_detected=[
            {
                "id": "VIOL-01",
                "standard": "OISD-137 Section 6.2",
                "severity": "High",
                "description": "Boiler Feed Pump P-101 emergency isolation valve response time delayed by 1.4 seconds beyond threshold.",
                "affected_asset": "P-101",
                "remediation": "Replace solenoid pilot valve and test closure speed."
            },
            {
                "id": "VIOL-02",
                "standard": "PESO Pressure Vessel Regulation 14",
                "severity": "Medium",
                "description": "Feedwater Tank T-301 safety relief valve re-certification due in 14 days.",
                "affected_asset": "T-301",
                "remediation": "Schedule bench calibration with certified inspector."
            }
        ],
        recommendations=[
            "Conduct quarterly emergency shutdown valve timing audits.",
            "Integrate automated PESO certification renewal triggers into AI Compliance Engine."
        ],
        audit_evidence_files=[
            "ISO_55001_Audit_Trail_2026.pdf",
            "OISD_137_Inspection_Certificate_Unit4.pdf",
            "P101_Calibration_Log.csv"
        ]
    )
