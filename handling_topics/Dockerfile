FROM python:3.11-slim

WORKDIR /app

COPY handling_topics/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY handling_topics /app/handling_topics
COPY kafka_pub_sub /app/kafka_pub_sub
COPY mongo /app/mongo
COPY elastic /app/elastic

CMD ["python","-m", "handling_topics.main"]
