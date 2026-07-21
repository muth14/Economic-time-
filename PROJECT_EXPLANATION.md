# INDUSTRIAL BRAIN: Complete Project Explanation & Architectural Guide

## 1. Executive Summary

**INDUSTRIAL BRAIN** ("The Unified Asset & Operations Intelligence Platform") is an enterprise-grade AI Operating System designed for industrial plants, chemical refineries, power generation facilities, and manufacturing infrastructure. 

It unifies fragmented plant documentation—such as P&ID engineering schematics, Flowserve/OEM operating manuals, sensor telemetry CSV logs, incident reports, and international safety compliance standards—into a **Living Knowledge Graph** paired with **Multi-Agentic Swarm Intelligence** and **Hybrid RAG (Retrieval-Augmented Generation)**.

---

## 2. Platform Architecture & Stack

```
                               ┌───────────────────────────────────────────────────────────┐
                               │   Next.js 14 Modern Enterprise UI Command Center          │
                               └─────────────────────────────┬─────────────────────────────┘
                                                             │ REST / WebSockets
                               ┌─────────────────────────────▼─────────────────────────────┐
                               │       FastAPI Dual-Mode AI Gateway Engine                 │
                               └─────────┬───────────────────┬───────────────────┬─────────┘
                                         │                   │                   │
               ┌─────────────────────────▼────┐    ┌─────────▼──────┐  ┌─────────▼─────────────────────┐
               │ Multi-Agent AI Swarm         │    │ Knowledge      │  │ Predictive Maintenance        │
               │ (Coordinator, Know, Doc,     │    │ Graph Engine   │  │ & What-If Simulator           │
               │  Compliance, RCA, Audit)     │    │ (Neo4j / Nx)   │  │ Engine                        │
               └──────────────────────────────┘    └────────────────┘  └───────────────────────────────┘
                                    │                      │                       │
             ┌──────────────────────┴──────────────────────┴───────────────────────┴──────┐
             │ PostgreSQL (Meta) | Qdrant (Vector) | Redis (Cache) | MinIO (Files)       │
             └────────────────────────────────────────────────────────────────────────────┘
```

### Technology Stack
- **Frontend**: Next.js 14 (App Router), React 18, TypeScript, Tailwind CSS, Framer Motion, Lucide Icons
- **Backend**: FastAPI, Python 3.11, Pydantic v2, NetworkX, Uvicorn, AsyncIO
- **Data & Middleware Layer**: PostgreSQL (Metadata), Neo4j (Graph), Qdrant (Vector Embeddings), Redis (Caching), MinIO (Object Storage)
- **Deployment**: Docker & Docker Compose (Single-command stack orchestration)

---

## 3. Dual-Mode Architecture

The platform features a **Dual-Mode Backend Resilience System**:
1. **Production Docker Stack**: Fully integrated with PostgreSQL, Neo4j, Qdrant, Redis, and MinIO.
2. **Self-Contained Local In-Memory Fallback**: When external database containers are offline, the backend seamlessly falls back to NetworkX in-memory graphs, SQLite metadata, and FAISS vector similarity. This guarantees that 100% of UI views, agent swarms, graph visualizers, and RAG copilot workflows run instantly out-of-the-box with zero setup friction.

---

## 4. Key Platform Modules & Capabilities

### Module 1: Universal Document Intelligence & P&ID Drawing Parser
- **Formats Supported**: PDF, DOCX, XLSX, CSV, P&ID schematics, and scanned handwritten forms.
- **P&ID Drawing Analysis**: Computer vision layout detection for equipment tags (`P-101`, `V-101`, `T-301`, `C-201`, `M-102`), pressure ratings, piping line numbers, and instrument loops.

### Module 2: Enterprise Living Knowledge Graph & Time Travel
- **Schema**: Nodes (`Equipment`, `Pump`, `Valve`, `Motor`, `Tank`, `Engineer`, `Vendor`, `Incident`, `Manual`, `Regulation`) and Edges (`CONNECTED_TO`, `FAILED_DUE_TO`, `MAINTAINED_BY`, `INSPECTED_BY`, `LOCATED_IN`).
- **Temporal Time Travel**: Timeline slider allowing plant managers to inspect graph topology evolution from commissioning (2021) to present live state (2026).

### Module 3: Industrial Evidence Copilot & Multi-Agent Swarm
- **Hybrid RAG**: Dense vector retrieval + BM25 keyword matching + multi-hop graph context expansion.
- **Explainability**: Verifiable citations with page numbers, exact text snippets, document deep-linking, and a **Trust Score Meter**.
- **Agent Swarm**:
  - `CoordinatorAgent`: Directs queries to domain agents.
  - `KnowledgeAgent`: Traverses entity connections.
  - `DocumentAgent`: Extracts text & tables.
  - `FailureAnalysisAgent`: Performs Root Cause Analysis (RCA).
  - `ComplianceAgent`: Audits regulatory rule breaches.

### Module 4: Asset Digital Twin & Predictive Maintenance (RUL)
- **Telemetry Processing**: Real-time sensor logs (Vibration RMS, temperature, pressure, seal flush pressure).
- **Weibull Degradation Forecasting**: Calculates Remaining Useful Life (RUL) in days and projects failure probability curves.
- **Equipment Chat**: Natural language interface per individual machine tag.

### Module 5: Root Cause Analysis (RCA) & Ishikawa Fishbone
- **Automated Fishbone Diagrams**: Auto-populates 6M categories (Machine, Method, Material, Manpower, Measurement, Milieu).
- **5-Why Tree**: Step-by-step causal chain breakdown for rapid incident resolution.

### Module 6: Compliance Intelligence & Audit Assistant
- **Regulations Monitored**: OISD-137, ISO 55001, PESO, Factory Act.
- **Violation Radar**: Real-time compliance breach detection and preventive action scheduling.

---

## 5. Directory Structure & Key Files

```
ET/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── endpoints/ (documents, graph, rag, copilot, rca, predictive, compliance, digital_twin, analytics)
│   │   │   └── router.py
│   │   ├── core/ (config, security, database)
│   │   ├── models/ (domain, schemas)
│   │   ├── services/ (document_processor, ocr_engine, pid_parser, knowledge_graph, vector_store, RAG_engine, agent_swarm)
│   │   ├── seed_data/ (generate_genchem_dataset.py, industrial_files_generator.py)
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── app/ (page.tsx workspace landing, documents, graph, copilot, digital-twin, rca, predictive, compliance, analytics)
│   │   ├── components/ (layout, ui, graph, twin, copilot, rca)
│   │   ├── context/ (WorkspaceContext.tsx)
│   │   ├── lib/ (api.ts, types.ts)
│   │   └── styles/ (globals.css)
│   ├── package.json
│   ├── tailwind.config.js
│   └── tsconfig.json
├── docker-compose.yml
├── README.md
├── .gitignore
└── PROJECT_EXPLANATION.md
```

---

## 6. How to Run locally

### Backend Setup:
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000
```
- API Swagger Docs: `http://127.0.0.1:8000/docs`

### Frontend Setup:
```bash
cd frontend
npm install
npm run dev
```
- Open browser at: `http://localhost:3000`

### Full Docker Stack Launch:
```bash
docker-compose up --build
```

---

## 7. Licensing & Attribution

Designed for high-reliability industrial operations, plant digital twin intelligence, and autonomous multi-agent engineering workflows.
