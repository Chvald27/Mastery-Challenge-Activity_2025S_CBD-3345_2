FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY news.py .

ENV NEWS_API_KEY=

CMD ["python", "news.py"]
