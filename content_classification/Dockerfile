FROM python:3.11-slim

WORKDIR /app

COPY content_classification/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY content_classification /app/content_classification
COPY services/elastic /app/services/elastic
COPY services/logger /app/services/logger
COPY services/kafka_pub_sub /app/services/kafka_pub_sub


CMD ["python","-m", "content_classification.main"]
