from app.services.agent_swarm import agent_swarm_service

def test_multi_agent_swarm_execution():
    task_res = agent_swarm_service.execute_swarm_task("Analyze Pump P-101 vibration anomaly", target_asset="P-101")
    assert task_res["status"] == "Completed"
    assert task_res["active_agent_count"] == 8
    assert len(task_res["collaboration_trace"]) >= 5
    assert "Elena Rostova" in str(task_res["collaboration_trace"]) or "Knowledge Agent" in str(task_res["collaboration_trace"])
