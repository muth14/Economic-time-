import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def build_pdf():
    pdf_filename = "Industrial_Knowledge_Intelligence_Unified_Asset_Operations_Brain.pdf"
    target_path = os.path.join(r"c:\Users\DELL\Downloads\ET", pdf_filename)

    doc = SimpleDocTemplate(
        target_path,
        pagesize=letter,
        leftMargin=0.6 * inch,
        rightMargin=0.6 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.6 * inch
    )

    styles = getSampleStyleSheet()

    # Custom Color Palette
    NAVY = colors.HexColor("#0F172A")
    BLUE = colors.HexColor("#2563EB")
    LIGHT_BLUE = colors.HexColor("#EFF6FF")
    SLATE = colors.HexColor("#475569")
    LIGHT_BG = colors.HexColor("#F8FAFC")
    BORDER_COLOR = colors.HexColor("#CBD5E1")
    DARK_TEXT = colors.HexColor("#1E293B")
    EMERALD_BG = colors.HexColor("#ECFDF5")
    EMERALD_BORDER = colors.HexColor("#10B981")
    PURPLE_BG = colors.HexColor("#F5F3FF")
    PURPLE_BORDER = colors.HexColor("#8B5CF6")
    AMBER_BG = colors.HexColor("#FFFBEB")
    AMBER_BORDER = colors.HexColor("#F59E0B")

    # Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=NAVY,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=BLUE,
        spaceAfter=12
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=NAVY,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=DARK_TEXT,
        spaceAfter=5
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        parent=body_style,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=4
    )

    arch_box_title = ParagraphStyle(
        'ArchTitle',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        alignment=1,
        textColor=NAVY
    )

    arch_box_desc = ParagraphStyle(
        'ArchDesc',
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        alignment=1,
        textColor=SLATE
    )

    story = []

    # Title Banner Block
    story.append(Paragraph("Industrial Knowledge Intelligence", title_style))
    story.append(Paragraph("Unified Asset & Operations Brain", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=BLUE, spaceBefore=0, spaceAfter=10))

    # Executive Overview Box
    exec_summary_text = Paragraph(
        "<b>Executive Summary:</b> An enterprise-grade AI Operating System for industrial knowledge intelligence, physical asset digital twinning, living Knowledge Graphs, hybrid RAG, multi-agent swarms, and predictive operations.",
        ParagraphStyle('ExecText', parent=body_style, fontSize=9, leading=13, textColor=NAVY)
    )
    exec_table = Table([[exec_summary_text]], colWidths=[7.3 * inch])
    exec_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 8),
        ('LINELEFT', (0,0), (-1,-1), 3, BLUE)
    ]))
    story.append(exec_table)
    story.append(Spacer(1, 8))

    # Section 1: Problem Statement
    story.append(Paragraph("1. Problem Statement", h1_style))
    story.append(Paragraph(
        "Modern industrial plants, oil refineries, chemical facilities, and power plants generate massive volumes of operational data. However, critical knowledge remains trapped in isolated organizational and technical silos, causing major operational risks:",
        body_style
    ))

    problems = [
        "<b>Fragmented Unstructured Knowledge:</b> Engineering P&ID schematics, OEM manuals, maintenance work orders, calibration records, and incident reports are scattered across paper scans, PDFs, and legacy servers.",
        "<b>Diagnostic Delays & Downtime Costs:</b> During critical plant alarms or equipment anomalies (e.g. pump vibration spikes), engineers spend hours manually searching manuals and past incident reports to locate root causes.",
        "<b>Expert Retirement & Knowledge Loss:</b> Decades of institutional experience held by senior field engineers are lost upon retirement without automated capture into structured plant memory.",
        "<b>Regulatory & Compliance Risks:</b> Verifying plant compliance against standards like OISD-137, ISO 55001, PESO, and Factory Acts requires tedious manual audits susceptible to human error.",
        "<b>Unpredictable Cascade Failures:</b> A single valve or pump failure can trigger unpredicted domino-effect chain reactions across interconnected process loops."
    ]
    for p in problems:
        story.append(Paragraph(f"• {p}", bullet_style))

    story.append(Spacer(1, 6))

    # Section 2: How It Was Developed
    story.append(Paragraph("2. How It Was Developed", h1_style))
    story.append(Paragraph(
        "The <b>Industrial Knowledge Intelligence (Industrial Brain)</b> platform was built following an end-to-end agile architecture methodology combining modern web engineering, graph algorithms, and autonomous multi-agent AI:",
        body_style
    ))

    dev_steps = [
        "<b>Domain Schema & Graph Modeling:</b> Designed an industrial entity-relationship ontology comprising 18 entity types (Pumps, Valves, Motors, Tanks, Engineers, Manuals, Failure Modes) and 10 relationship types (CONNECTED_TO, FAILED_DUE_TO, MAINTAINED_BY).",
        "<b>Universal Document & P&ID Parser Construction:</b> Developed computer vision spatial tag detection and OCR layout algorithms to extract equipment tags (P-101, V-101), pressure ratings, and line connections directly from CAD/PDF schematics.",
        "<b>Dual-Mode Backend Architecture:</b> Built a FastAPI gateway with automated fallbacks (Neo4j/Postgres/Qdrant cloud containers vs. in-memory NetworkX/SQLite/FAISS) ensuring zero-setup local execution.",
        "<b>Autonomous Multi-Agent Swarm Orchestration:</b> Implemented a 7-agent swarm (Coordinator, Knowledge, Document, Maintenance, Compliance, RCA, Audit) using AsyncIO parallel consensus.",
        "<b>Hybrid RAG & Grounded Evidence Engine:</b> Combined dense vector similarity search, BM25 keyword matching, and multi-hop graph traversal to generate answers backed by exact document page citations and a live Trust Meter.",
        "<b>Next.js 14 Command Center UI:</b> Constructed a modern glassmorphic web dashboard with interactive force-directed graph canvases, Time Travel timeline sliders, 3D plant digital twins, and Ishikawa fishbone generators."
    ]
    for step in dev_steps:
        story.append(Paragraph(f"• {step}", bullet_style))

    story.append(Spacer(1, 6))

    # Section 3: Technology Stack
    story.append(Paragraph("3. Technology Stack", h1_style))
    
    stack_data = [
        [Paragraph("<b>Layer</b>", body_style), Paragraph("<b>Technologies & Libraries Used</b>", body_style)],
        [Paragraph("<b>Frontend UI</b>", body_style), Paragraph("Next.js 14 (App Router), React 18, TypeScript, Tailwind CSS, Framer Motion, Lucide Icons", body_style)],
        [Paragraph("<b>Backend Gateway</b>", body_style), Paragraph("FastAPI, Python 3.11, Pydantic v2, NetworkX, Uvicorn, AsyncIO", body_style)],
        [Paragraph("<b>Graph Database</b>", body_style), Paragraph("Neo4j Graph Database + NetworkX In-Memory Fallback Engine", body_style)],
        [Paragraph("<b>Vector & RAG Engine</b>", body_style), Paragraph("Qdrant Vector DB, SentenceTransformers, BM25 Keyword Search, FAISS", body_style)],
        [Paragraph("<b>Relational & Cache</b>", body_style), Paragraph("PostgreSQL (Metadata & Audit Trails), Redis (Session Caching)", body_style)],
        [Paragraph("<b>Object Storage</b>", body_style), Paragraph("MinIO / Local Object Storage for raw PDFs, DOCX, and P&ID schematics", body_style)],
        [Paragraph("<b>Orchestration</b>", body_style), Paragraph("Docker, Docker Compose, Pytest test suite", body_style)]
    ]

    stack_table = Table(stack_data, colWidths=[1.7 * inch, 5.6 * inch])
    stack_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), LIGHT_BG),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE')
    ]))
    story.append(stack_table)

    story.append(Spacer(1, 8))

    # Section 4: Innovation & Uniqueness
    story.append(Paragraph("4. Innovation & Uniqueness", h1_style))
    story.append(Paragraph(
        "Industrial Brain sets a new benchmark for enterprise industrial AI by introducing several key innovations:",
        body_style
    ))

    innovations = [
        "<b>Graph Time Travel (Temporal Topology Evolution):</b> Drag a timeline slider from 2021 (commissioning) to 2026 to visually inspect how asset relationships, maintenance events, and failure risks evolved over time.",
        "<b>Dual-Mode Zero-Friction Resilience:</b> Operates seamlessly in full enterprise Docker environments or self-contained local in-memory mode without requiring external database setups or cloud API keys.",
        "<b>Spatial P&ID Drawing Entity Highlighter:</b> Auto-extracts tag bounding boxes from complex engineering schematics, allowing engineers to click tags to immediately inspect live telemetry and connected manuals.",
        "<b>Predictive Weibull Degradation & RUL Forecasting:</b> Computes Remaining Useful Life (RUL) in days and predicts failure probability curves using sensor telemetry (Vibration RMS, temperatures, seal flush pressures).",
        "<b>What-If Failure Cascade Risk Simulator:</b> Enables engineers to simulate hypothetical component breakdowns (e.g. Valve V-101 failing closed) and instantly visualize predicted domino-effect chain reactions across connected equipment.",
        "<b>Auto Ishikawa Fishbone & 5-Why RCA Generator:</b> Automatically converts incident logs and sensor anomalies into interactive Fishbone (6M) cause-and-effect diagrams.",
        "<b>Grounded Citation & Trust Meter Engine:</b> Every AI response includes exact document page citations, text snippets, confidence scores, and multi-agent execution traces."
    ]
    for inn in innovations:
        story.append(Paragraph(f"• {inn}", bullet_style))

    story.append(Spacer(1, 8))

    # Section 5: Architecture Diagram (Clean Flowable Cards)
    story.append(Paragraph("5. System Architecture Diagram", h1_style))
    story.append(Paragraph(
        "The diagram below illustrates the clean modular architecture of the Industrial Brain platform:",
        body_style
    ))

    # Building visually appealing architecture blocks table
    top_box_content = [
        Paragraph("<b>NEXT.JS 14 MODERN ENTERPRISE UI COMMAND CENTER</b>", arch_box_title),
        Paragraph("Executive Dashboard • P&ID Viewer • Graph Visualizer • Copilot • Digital Twin Explorer", arch_box_desc)
    ]
    top_table = Table([[top_box_content]], colWidths=[7.3 * inch])
    top_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BLUE),
        ('BOX', (0,0), (-1,-1), 1.5, BLUE),
        ('PADDING', (0,0), (-1,-1), 6)
    ]))

    arrow1 = Paragraph("<b>↓ REST APIs & WebSockets</b>", ParagraphStyle('Arr1', parent=arch_box_desc, fontName='Helvetica-Bold', textColor=BLUE))

    mid_box_content = [
        Paragraph("<b>FASTAPI DUAL-MODE AI GATEWAY ENGINE</b>", arch_box_title),
        Paragraph("API Routing • Security & Auth • Universal Document Ingest • Multi-Agent Workflow Coordinator", arch_box_desc)
    ]
    mid_table = Table([[mid_box_content]], colWidths=[7.3 * inch])
    mid_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, SLATE),
        ('PADDING', (0,0), (-1,-1), 6)
    ]))

    arrow2 = Paragraph("<b>↓ Parallel Async Orchestration</b>", ParagraphStyle('Arr2', parent=arch_box_desc, fontName='Helvetica-Bold', textColor=SLATE))

    # 3 Parallel Engine Cards
    c1 = [
        Paragraph("<b>Autonomous Multi-Agent Swarm</b>", arch_box_title),
        Paragraph("Coordinator, Knowledge, Document, Maintenance, Compliance, RCA & Audit Agents", arch_box_desc)
    ]
    c2 = [
        Paragraph("<b>Living Knowledge Graph & RAG</b>", arch_box_title),
        Paragraph("Neo4j / NetworkX Multi-Hop Traversal + Qdrant Dense Vector & BM25 Keyword Search", arch_box_desc)
    ]
    c3 = [
        Paragraph("<b>Predictive Maintenance & What-If</b>", arch_box_title),
        Paragraph("Weibull RUL Forecasting + Failure Probability Curves & Cascade Risk Simulator", arch_box_desc)
    ]

    three_col_table = Table([[c1, c2, c3]], colWidths=[2.36 * inch, 2.36 * inch, 2.36 * inch])
    three_col_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), PURPLE_BG),
        ('BOX', (0,0), (0,0), 1, PURPLE_BORDER),
        ('BACKGROUND', (1,0), (1,0), EMERALD_BG),
        ('BOX', (1,0), (1,0), 1, EMERALD_BORDER),
        ('BACKGROUND', (2,0), (2,0), AMBER_BG),
        ('BOX', (2,0), (2,0), 1, AMBER_BORDER),
        ('PADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP')
    ]))

    arrow3 = Paragraph("<b>↓ Unified Storage Interface</b>", ParagraphStyle('Arr3', parent=arch_box_desc, fontName='Helvetica-Bold', textColor=SLATE))

    bottom_box_content = [
        Paragraph("<b>ENTERPRISE STORAGE & MIDDLEWARE LAYER</b>", arch_box_title),
        Paragraph("PostgreSQL (Metadata & Audits) • Neo4j (Graph) • Qdrant (Vectors) • Redis (Cache) • MinIO (Files)", arch_box_desc)
    ]
    bottom_table = Table([[bottom_box_content]], colWidths=[7.3 * inch])
    bottom_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, SLATE),
        ('PADDING', (0,0), (-1,-1), 6)
    ]))

    arch_flowables = [
        top_table,
        Spacer(1, 3),
        arrow1,
        Spacer(1, 3),
        mid_table,
        Spacer(1, 3),
        arrow2,
        Spacer(1, 3),
        three_col_table,
        Spacer(1, 3),
        arrow3,
        Spacer(1, 3),
        bottom_table
    ]

    story.append(KeepTogether(arch_flowables))
    story.append(Spacer(1, 10))

    # Footer
    footer_note = Paragraph("Document Generated: Industrial Brain System Architecture • Unified Asset & Operations Intelligence", ParagraphStyle('Foot', parent=body_style, fontSize=8, textColor=SLATE, alignment=1))
    story.append(footer_note)

    doc.build(story)
    print(f"Successfully generated PDF at: {target_path}")

if __name__ == "__main__":
    build_pdf()
