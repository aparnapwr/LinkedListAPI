ARG PYTHON_VERSION=3.11-slim
FROM python:${PYTHON_VERSION}
#base image to use for building a Docker container

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
#run a FastAPI application using Uvicorn server


