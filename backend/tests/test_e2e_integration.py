import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_e2e_root_health():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "Online"
    assert data["version"] == "1.0.0"

def test_e2e_copilot_rag_query():
    payload = {"query": "Why did Pump P-101 fail vibration test?", "asset_id": "P-101"}
    response = client.post("/api/v1/copilot/query", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert len(data["citations"]) > 0
    assert len(data["reasoning_chain"]) > 0
    assert data["confidence_score"] > 80.0

def test_e2e_knowledge_graph():
    response = client.get("/api/v1/graph/")
    assert response.status_code == 200
    data = response.json()
    assert len(data["nodes"]) > 0
    assert len(data["edges"]) > 0

def test_e2e_predictive_heatmap_and_whatif():
    heatmap_res = client.get("/api/v1/predictive/heatmap")
    assert heatmap_res.status_code == 200
    assert len(heatmap_res.json()) >= 4

    whatif_res = client.post("/api/v1/predictive/what-if", json={"trigger_entity_id": "V-101", "failure_mode": "Actuator Jam"})
    assert whatif_res.status_code == 200
    whatif_data = whatif_res.json()
    assert whatif_data["trigger_entity"] == "V-101"
    assert len(whatif_data["cascade_chain"]) >= 2

def test_e2e_rca_fishbone():
    rca_res = client.get("/api/v1/rca/analyze/P-101")
    assert rca_res.status_code == 200
    rca_data = rca_res.json()
    assert len(rca_data["fishbone"]) >= 5
    assert len(rca_data["five_whys"]) >= 5

def test_e2e_compliance_and_twin():
    comp_res = client.get("/api/v1/compliance/report")
    assert comp_res.status_code == 200
    assert comp_res.json()["compliance_score"] > 80.0

    twin_res = client.get("/api/v1/twin/P-101")
    assert twin_res.status_code == 200
    assert twin_res.json()["asset_id"] == "P-101"

def test_e2e_equipment_dna():
    dna_res = client.get("/api/v1/twin/dna/P-101")
    assert dna_res.status_code == 200
    data = dna_res.json()
    assert data["asset_id"] == "P-101"
    assert "DNA-" in data["dna_fingerprint"]
    assert len(data["timeline"]) >= 3

def test_e2e_industrial_memory_and_cross_plant():
    mem_payload = {
        "asset_id": "P-101",
        "engineer_name": "Elena Rostova",
        "feedback_correction": "API Plan 53B pressure check verified",
        "verified_root_cause": "Seal fluid pressure leakage"
    }
    mem_res = client.post("/api/v1/innovations/memory", json=mem_payload)
    assert mem_res.status_code == 200
    assert mem_res.json()["status"] == "Success"

    cp_res = client.get("/api/v1/innovations/cross-plant")
    assert cp_res.status_code == 200
    assert len(cp_res.json()) >= 1

def test_e2e_plant_doctor_and_executive_decision():
    doc_res = client.get("/api/v1/innovations/plant-doctor")
    assert doc_res.status_code == 200
    assert doc_res.json()["estimated_financial_loss_usd"] > 0

    exec_res = client.get("/api/v1/innovations/executive-decision/P-101")
    assert exec_res.status_code == 200
    exec_data = exec_res.json()
    assert len(exec_data["options"]) == 3
    assert any(opt["is_recommended"] for opt in exec_data["options"])

def test_e2e_explainability_dashboard():
    exp_res = client.get("/api/v1/copilot/explainability/Q-99841")
    assert exp_res.status_code == 200
    exp_data = exp_res.json()
    assert len(exp_data["sources_used"]) >= 2
    assert exp_data["confidence_breakdown"]["Composite Trust Score"] > 90.0

