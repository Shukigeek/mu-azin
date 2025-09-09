FROM python:3.11-slim

WORKDIR /app

COPY content_classification/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY content_classification /app/content_classification
COPY elastic /app/elastic
COPY logger /app/logger


CMD ["python","-m", "handel_files.main"]
