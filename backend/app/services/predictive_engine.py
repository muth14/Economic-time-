import math
from typing import Dict, Any, List
from app.models.schemas import WhatIfResponse, WhatIfCascadeStep, SOPResponse, RiskRadarData
from app.services.knowledge_graph import kg_service
from app.seed_data.seed_data import SAMPLE_ASSETS

class PredictiveEngineService:
    @staticmethod
    def calculate_weibull_failure_probability(operating_days: float, scale_eta: float = 365.0, shape_beta: float = 2.5) -> float:
        """
        Calculates Weibull cumulative distribution failure probability:
        F(t) = 1 - exp( - (t / eta) ^ beta )
        """
        if operating_days <= 0:
            return 0.0
        exponent = (operating_days / scale_eta) ** shape_beta
        prob = 1.0 - math.exp(-exponent)
        return round(min(0.99, max(0.01, prob)), 4)

    @staticmethod
    def calculate_rul_days(vibration_rms: float, max_rms_threshold: float = 8.5, baseline_rms: float = 2.0) -> int:
        """
        Estimates Remaining Useful Life (RUL in days) based on linear degradation rate:
        RUL = (Threshold - Current) / DegradationSlope
        """
        if vibration_rms >= max_rms_threshold:
            return 0
        degradation_rate_per_day = 0.15  # mm/s degradation per day
        remaining = (max_rms_threshold - vibration_rms) / degradation_rate_per_day
        return max(1, int(remaining))

    def get_plant_risk_heatmap(self) -> List[Dict[str, Any]]:
        heatmap = []
        areas = [
            {"grid_id": "BAY-1", "area_name": "Unit 4 Utility & Boiler Bay", "asset_ids": ["P-101", "M-102"]},
            {"grid_id": "BAY-2", "area_name": "Steam Header Line 2", "asset_ids": ["V-101"]},
            {"grid_id": "BAY-3", "area_name": "Hydrocracker Unit B", "asset_ids": ["C-201"]},
            {"grid_id": "BAY-4", "area_name": "Utilities Tank Farm South", "asset_ids": ["T-301"]}
        ]

        for area in areas:
            health_sum = 0
            count = 0
            for a_id in area["asset_ids"]:
                for sa in SAMPLE_ASSETS:
                    if sa["id"] == a_id:
                        health_sum += sa["health_score"]
                        count += 1
            avg_health = health_sum / max(1, count)
            risk_level = "Red" if avg_health < 50 else ("Orange" if avg_health < 70 else ("Yellow" if avg_health < 80 else "Green"))
            
            heatmap.append({
                "grid_id": area["grid_id"],
                "area_name": area["area_name"],
                "asset_ids": area["asset_ids"],
                "risk_level": risk_level,
                "avg_health_score": round(avg_health, 2)
            })
        return heatmap

    def simulate_what_if_failure(self, entity_id: str, failure_mode: str) -> WhatIfResponse:
        e_upper = entity_id.upper()
        # Retrieve graph neighborhood to trace real topology propagation
        full_graph = kg_service.get_full_graph()
        connected_edges = [e for e in full_graph["edges"] if e["source"] == e_upper or e["target"] == e_upper]

        cascade_steps = [
            WhatIfCascadeStep(
                step=1,
                entity_id=e_upper,
                entity_name=f"Primary Trigger Asset {e_upper}",
                impact_level="Severe",
                consequence=f"Asset {e_upper} experience [{failure_mode}] causing immediate local trip.",
                time_to_impact="T + 0 min"
            )
        ]

        step_counter = 2
        for edge in connected_edges[:3]:
            other = edge["target"] if edge["source"] == e_upper else edge["source"]
            if other != e_upper:
                cascade_steps.append(
                    WhatIfCascadeStep(
                        step=step_counter,
                        entity_id=other,
                        entity_name=f"Connected Asset {other}",
                        impact_level="High" if step_counter == 2 else "Moderate",
                        consequence=f"Secondary pressure differential & hydraulic surge propagated via {edge['type']} relationship.",
                        time_to_impact=f"T + {step_counter * 4} min"
                    )
                )
                step_counter += 1

        est_downtime = round(step_counter * 3.5 + 4.0, 1)
        est_financial_loss = round(est_downtime * 18500.0, 2)

        return WhatIfResponse(
            trigger_entity=e_upper,
            cascade_chain=cascade_steps,
            total_plant_downtime_est_hours=est_downtime,
            est_financial_loss_usd=est_financial_loss,
            mitigation_strategy=[
                f"Isolate line feed connected to {e_upper} within 3 minutes of alarm.",
                "Engage auxiliary standby recirculation manifold loop.",
                "Execute emergency maintenance protocol SOP-12."
            ]
        )

    def generate_sop(self, asset_id: str, procedure_type: str) -> SOPResponse:
        return SOPResponse(
            procedure_title=f"Standard Operating Procedure: {procedure_type} for Asset {asset_id}",
            asset_id=asset_id,
            steps=[
                {"step_num": 1, "action": "Lock Out Tag Out (LOTO)", "detail": "Isolate high voltage feeder breakers and depressurize suction line to 0 bar."},
                {"step_num": 2, "action": "Drain Lubricant Reservoir", "detail": "Collect fluid sample in ISO container for spectrographic wear particle analysis."},
                {"step_num": 3, "action": "Extract Mechanical Seal Cartridge", "detail": "Torque coupling bolts to 140 N-m using calibrated digital torque wrench."},
                {"step_num": 4, "action": "Post-Maintenance Laser Realignment", "detail": "Verify radial and axial runout within <0.02 mm before energizing."}
            ],
            required_tools=["Laser Alignment Kit", "Calibrated Torque Wrench (200 Nm)", "API Plan 53B Flush Cart"],
            safety_ppe=["Nitrile Gloves", "Arc Flash Suit Category 2", "Safety Goggles", "Steel Toe Boots"],
            generated_at="2026-07-20 22:24:00"
        )

    def get_risk_radar(self) -> RiskRadarData:
        high_risk = []
        for a in SAMPLE_ASSETS:
            if a["health_score"] < 75:
                high_risk.append({"id": a["id"], "name": a["name"], "health": a["health_score"], "risk": a["risk_level"]})

        return RiskRadarData(
            overall_enterprise_risk_index=38.4,
            high_risk_assets=high_risk,
            compliance_gap_count=2,
            overdue_maintenances=1,
            live_alerts=[
                {"severity": "Critical", "message": "Valve V-101 stem friction index exceeds 85%", "timestamp": "10 mins ago"},
                {"severity": "Warning", "message": "Pump P-101 bearing temperature DE reached 78.4°C", "timestamp": "25 mins ago"}
            ]
        )

predictive_service = PredictiveEngineService()
