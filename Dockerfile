FROM python:3.10-slim
WORKDIR /fastapi
COPY req.txt .
RUN pip install --upgrade pip
RUN pip install -r req.txt
COPY . .
WORKDIR /src
CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000