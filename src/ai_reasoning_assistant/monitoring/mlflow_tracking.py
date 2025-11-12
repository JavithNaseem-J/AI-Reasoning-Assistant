import mlflow

def init_mlflow():
    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("Agentic-RAG-Assistant")

def log_metrics(query, score, latency):
    with mlflow.start_run():
        mlflow.log_param("query", query)
        mlflow.log_metric("confidence_score", score)
        mlflow.log_metric("latency", latency)
