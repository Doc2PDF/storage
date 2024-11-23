FROM python:3.12-slim

RUN mkdir output

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 11011

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "11011"]
