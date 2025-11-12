# ---------- BASE IMAGE ----------
FROM python:3.11-slim

# ---------- SETUP ENV ----------
WORKDIR /app
COPY . /app

# ---------- INSTALL DEPENDENCIES ----------
RUN pip install --no-cache-dir -r requirements.txt

# ---------- EXPOSE PORT ----------
EXPOSE 8501

# ---------- START STREAMLIT ----------
CMD ["streamlit", "run", "app/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
