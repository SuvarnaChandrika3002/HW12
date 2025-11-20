FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV DATABASE_URL=postgresql://user:pass@db:5432/appdb

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
