# INDUSTRIAL BRAIN: The Unified Asset & Operations Intelligence Platform

> **An Enterprise AI Operating System for Industrial Knowledge Intelligence, Physical Asset Digital Twinning, Knowledge Graphs, Hybrid RAG, Multi-Agent Swarms, and Predictive Operations.**

📖 **For a full architectural & technical breakdown, see [PROJECT_EXPLANATION.md](PROJECT_EXPLANATION.md).**

---


## Architecture Diagram

```
                              ┌───────────────────────────────────────────────┐
                              │    Next.js 14 Glassmorphic UI Command Center  │
                              └───────────────────────┬───────────────────────┘
                                                      │ REST / WebSockets
                              ┌───────────────────────▼───────────────────────┐
                              │    FastAPI Dual-Mode AI Gateway Engine        │
                              └───────┬───────────────┬───────────────┬───────┘
                                      │               │               │
            ┌─────────────────────────▼──┐     ┌──────▼───────┐ ┌─────▼────────────────────┐
            │ Autonomous Multi-Agent Swarm│     │ Knowledge    │ │ Predictive Maintenance    │
            │ (Coordinator, Know, Doc,    │     │ Graph Engine │ │ & What-If Simulator       │
            │  Compliance, RCA, Audit)    │     │ (Neo4j / Nx) │ │ Engine                    │
            └────────────────────────────┘     └──────────────┘ └───────────────────────────┘
                                 │                    │                       │
           ┌─────────────────────┴────────────────────┴───────────────────────┴──┐
           │ PostgreSQL (Meta) | Qdrant (Vector) | Redis (Cache) | MinIO (Files)  │
           └──────────────────────────────────────────────────────────────────────┘
```

---

## Key Highlights

- **20 Core Modules Included**:
  1. Universal Document Intelligence (PDF, DOCX, PPT, P&ID schematics, CSV, Scanned forms)
  2. OCR Intelligence (Handwritten, typed, forms, stamps, signatures)
  3. Knowledge Graph Engine (Nodes: Pump, Valve, Motor, Engineer, Vendor, Incident, Manual; Edges: CONNECTED_TO, FAILED_DUE_TO, MAINTAINED_BY)
  4. Enterprise Hybrid RAG (Vector + BM25 + Graph reasoning with Trust Meter & document citations)
  5. Industrial Copilot (Multimodal ChatGPT-style assistant with voice, image, file uploads)
  6. Root Cause Analysis Agent (Automated Ishikawa Fishbone diagram & 5-Why tree)
  7. Predictive Maintenance Agent (RUL forecasting, failure probability curves, maintenance calendar)
  8. Compliance Intelligence (ISO 55001, OISD-137, PESO, Factory Act violation radar)
  9. Lessons Learned Engine (Past incident pattern matcher & recommendation generator)
  10. Knowledge Timeline (Equipment lifecycle timeline from installation to failure)
  11. Asset Digital Twin (Telemetry gauges, connected asset graph, OEM specs)
  12. Voice Assistant (Field engineer hands-free speech-to-text mode)
  13. Agentic AI Swarm (8 autonomous collaborating agents)
  14. Workflow Automation (Upload → OCR → Entity Extractor → KG update → Vector Index → Risk alert)
  15. Executive Analytics Dashboard (Metrics, downtime trends, failure category breakdowns)
  16. Notifications (Critical failure, compliance alerts)
  17. Global Search (Cross-entity instant search)
  18. Built-in Document Viewer (Entity bounding box highlighter)
  19. Admin Panel & Role RBAC
  20. Field Engineer Mobile Mode

- **20 Hackathon Innovations Built-In**:
  - **AI Memory Graph**, **Plant Failure Prediction Heatmap**, **What-If Cascade Simulator**, **Natural Language Graph Explorer**, **AI SOP Generator**, **Industrial Wikipedia**, **Knowledge Drift Detector**, **Expert Retirement Preservation**, **Auto Incident Story Narrative**, **Risk Radar**, **Equipment Chatbot**, **Graph Time Travel**, and **Autonomous Audit Assistant**.

---

## Tech Stack

- **Frontend**: Next.js 14, React 18, TypeScript, Tailwind CSS, Framer Motion, Lucide Icons
- **Backend**: FastAPI, Python 3.11, Pydantic, NetworkX, Uvicorn
- **Databases & Middleware**: PostgreSQL, Neo4j, Qdrant, Redis, MinIO
- **Deployment**: Docker, Docker Compose

---

## Quickstart Guide

### 1. Dual-Mode Instant Launch (Without Docker)

#### Backend:
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000
```
API Swagger Docs will be available at: `http://localhost:8000/docs`

#### Frontend:
```bash
cd frontend
npm install
npm run dev
```
Open application in browser at: `http://localhost:3000`

---

### 2. Enterprise Docker Stack Launch

```bash
docker-compose up --build
```
This launches PostgreSQL, Neo4j, Qdrant, Redis, MinIO, FastAPI, and Next.js automatically.
