FROM python:3.11-slim

WORKDIR /app

COPY handling_topics/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY handling_topics /app/handling_topics
COPY services/kafka_pub_sub /app/services/kafka_pub_sub
COPY services/mongo /app/services/mongo
COPY services/elastic /app/services/elastic
COPY services/logger /app/services/logger

CMD ["python","-m", "handling_topics.main"]
