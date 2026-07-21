from fastapi import APIRouter
from app.api.endpoints import auth, documents, graph, copilot, predictive, rca, compliance, digital_twin, innovations, analytics

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(documents.router, prefix="/documents", tags=["Universal Document Intelligence"])
api_router.include_router(graph.router, prefix="/graph", tags=["Knowledge Graph"])
api_router.include_router(copilot.router, prefix="/copilot", tags=["Industrial RAG Copilot"])
api_router.include_router(predictive.router, prefix="/predictive", tags=["Predictive Maintenance & Heatmap"])
api_router.include_router(rca.router, prefix="/rca", tags=["Root Cause Analysis"])
api_router.include_router(compliance.router, prefix="/compliance", tags=["Compliance Intelligence"])
api_router.include_router(digital_twin.router, prefix="/twin", tags=["Asset Digital Twin"])
api_router.include_router(innovations.router, prefix="/innovations", tags=["Hackathon Innovations"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["Executive Analytics Dashboard"])
