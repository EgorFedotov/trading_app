FROM python:3.10
WORKDIR /fastapi
COPY req.txt .
RUN pip install --upgrade pip
RUN pip install -r req.txt
COPY . .
RUN chmod a+x docker/*.sh
# WORKDIR src
# CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000