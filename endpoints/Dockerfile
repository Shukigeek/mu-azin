FROM python:3.11-slim

WORKDIR /app

COPY endpoints/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY endpoints /app/endpoints
COPY services/elastic /app/services/elastic
COPY services/logger /app/services/logger

CMD ["uvicorn", "endpoints.app:app", "--host", "0.0.0.0", "--port", "8005"]
