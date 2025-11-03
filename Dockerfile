FROM python:3.12-slim AS base
WORKDIR /app
COPY app.py languages.txt ./
RUN pip install --no-cache-dir fastapi uvicorn gunicorn
EXPOSE 8080
USER 1001
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "2", "-b", "0.0.0.0:8080", "app:app"]
