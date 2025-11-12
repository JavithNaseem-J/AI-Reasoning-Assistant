from fastapi import FastAPI
from agents.orchestrator_agent import OrchestratorAgent
from monitoring.mlflow_tracking import log_metrics
import time

app = FastAPI(title="AI Reasoning Assistant API")
agent = OrchestratorAgent()

@app.get("/ask")
async def ask(query: str):
    start = time.time()
    result = agent.run_pipeline(query)
    latency = time.time() - start
    log_metrics(query, 0.9, latency)
    return result
