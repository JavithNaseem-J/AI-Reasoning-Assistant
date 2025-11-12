from fastapi import APIRouter, Query
from agents.orchestrator_agent import OrchestratorAgent
from monitoring.mlflow_tracking import log_metrics
from core.logger import log_request_start, log_request_latency
import time

router = APIRouter(prefix="/query", tags=["Query"])

agent = OrchestratorAgent()

@router.get("/ask")
async def ask_question(query: str = Query(..., description="User query text")):
    log_request_start()
    start = time.time()

    result = agent.run_pipeline(query)
    latency = time.time() - start

    log_request_latency(latency)
    log_metrics(query, 0.9, latency)

    return result
