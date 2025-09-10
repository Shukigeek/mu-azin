FROM python:3.11-slim

WORKDIR /app

COPY STT/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY STT /app/STT
COPY services/mongo /app/services/mongo
COPY services/kafka_pub_sub /app/services/kafka_pub_sub
COPY services/elastic /app/services/elastic
COPY services/logger /app/services/logger


CMD ["python","-m", "STT.main"]
