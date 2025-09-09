FROM python:3.11-slim

WORKDIR /app

COPY handling_topics/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY STT /app/STT
COPY mongo /app/mongo
COPY elastic /app/elastic
COPY logger /app/logger
COPY read_recoreds /app/read_recoreds

CMD ["python","-m", "STT.main"]
