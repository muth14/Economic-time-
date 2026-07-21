import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import json
import tracemalloc
from fastapi.testclient import TestClient
from app.main import app
from app.services.knowledge_graph import kg_service
from app.services.RAG_engine import rag_service
from app.services.predictive_engine import predictive_service
from app.services.agent_swarm import agent_swarm_service

client = TestClient(app)

def run_benchmarks():
    results = {}

    # Benchmark 1: Copilot Query
    tracemalloc.start()
    t0 = time.perf_counter()
    res_copilot = client.post("/api/v1/copilot/query", json={"query": "Why did Pump P-101 fail vibration test?", "asset_id": "P-101"})
    t1 = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    results["copilot"] = {
        "status_code": res_copilot.status_code,
        "latency_ms": round((t1 - t0) * 1000, 2),
        "peak_memory_kb": round(peak_mem / 1024, 2),
        "input": {"query": "Why did Pump P-101 fail vibration test?", "asset_id": "P-101"},
        "output_summary": res_copilot.json()["answer"][:120] + "...",
        "citations_count": len(res_copilot.json()["citations"]),
        "confidence_score": res_copilot.json()["confidence_score"]
    }

    # Benchmark 2: Knowledge Graph
    tracemalloc.start()
    t0 = time.perf_counter()
    res_graph = client.get("/api/v1/graph/?query=P-101")
    t1 = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    results["knowledge_graph"] = {
        "status_code": res_graph.status_code,
        "latency_ms": round((t1 - t0) * 1000, 2),
        "peak_memory_kb": round(peak_mem / 1024, 2),
        "nodes_count": len(res_graph.json()["nodes"]),
        "edges_count": len(res_graph.json()["edges"])
    }

    # Benchmark 3: Predictive What-If
    tracemalloc.start()
    t0 = time.perf_counter()
    res_whatif = client.post("/api/v1/predictive/what-if", json={"trigger_entity_id": "V-101", "failure_mode": "Actuator Diaphragm Rupture"})
    t1 = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    results["what_if"] = {
        "status_code": res_whatif.status_code,
        "latency_ms": round((t1 - t0) * 1000, 2),
        "peak_memory_kb": round(peak_mem / 1024, 2),
        "est_downtime_hours": res_whatif.json()["total_plant_downtime_est_hours"],
        "est_financial_loss_usd": res_whatif.json()["est_financial_loss_usd"]
    }

    # Benchmark 4: Multi-Agent Swarm
    tracemalloc.start()
    t0 = time.perf_counter()
    res_swarm = client.post("/api/v1/innovations/agent-swarm", json={"prompt": "Audit Pump P-101", "target_asset": "P-101"})
    t1 = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    results["agent_swarm"] = {
        "status_code": res_swarm.status_code,
        "latency_ms": round((t1 - t0) * 1000, 2),
        "peak_memory_kb": round(peak_mem / 1024, 2),
        "active_agent_count": res_swarm.json()["active_agent_count"],
        "trace_steps": len(res_swarm.json()["collaboration_trace"])
    }

    print("BENCHMARK_EVIDENCE_JSON:" + json.dumps(results, indent=2))

if __name__ == "__main__":
    run_benchmarks()
