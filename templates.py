import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

project_name = "ai_reasoning_assistant"

list_of_files = [
    "config/config.yaml",
    "config/params.yaml",
    ".env",
    "pyproject.toml",
    "Dockerfile",
    "docker/docker-compose.yml",

    f"src/{project_name}/__init__.py",

    f"src/{project_name}/agents/__init__.py",
    f"src/{project_name}/agents/retriever_agent.py",
    f"src/{project_name}/agents/analyzer_agent.py",
    f"src/{project_name}/agents/summarizer_agent.py",
    f"src/{project_name}/agents/evaluator_agent.py",
    f"src/{project_name}/agents/orchestrator_agent.py",

    f"src/{project_name}/core/__init__.py",
    f"src/{project_name}/core/embedder.py",
    f"src/{project_name}/core/rag_pipeline.py",
    f"src/{project_name}/core/memory_graph.py",
    f"src/{project_name}/core/prompt_templates.py",
    f"src/{project_name}/core/logger.py",

    f"src/{project_name}/api/__init__.py",
    f"src/{project_name}/api/main.py",
    f"src/{project_name}/api/routes/__init__.py",
    f"src/{project_name}/api/routes/query_route.py",
    f"src/{project_name}/api/routes/feedback_route.py",
    f"src/{project_name}/api/routes/metrics_route.py",
    f"src/{project_name}/api/utils/__init__.py",
    f"src/{project_name}/api/utils/database.py",
    f"src/{project_name}/api/utils/schemas.py",

    f"src/{project_name}/monitoring/__init__.py",
    f"src/{project_name}/monitoring/mlflow_tracking.py",

    f"src/{project_name}/app/__init__.py",
    f"src/{project_name}/app/streamlit_app.py",

    "data/docs/.gitkeep",
    "data/embeddings/.gitkeep",
    "notebooks/experimentation.ipynb",
]


for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory: {file_dir}")

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, "w") as f:
            pass
        logging.info(f"Created file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")

