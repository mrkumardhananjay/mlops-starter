# The delivery time service in a container.
FROM python:3.12-slim

WORKDIR /app

# Libraries first: this layer is reused until requirements.txt changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Code and model last: these change most often.
COPY app.py model.joblib ./

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
