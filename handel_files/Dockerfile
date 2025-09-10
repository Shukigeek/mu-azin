FROM python:3.11-slim

WORKDIR /app

COPY handel_files/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY handel_files /app/handel_files
COPY services/kafka_pub_sub /app/services/kafka_pub_sub
COPY services/logger /app/services/logger


CMD ["python","-m", "handel_files.main"]
