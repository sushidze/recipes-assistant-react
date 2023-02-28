FROM python:3.8

WORKDIR /app

COPY ../ /app

RUN python -m pip install --upgrade pip
RUN pip install -r /app/backend/requirements.txt --no-cache-dir
RUN chmod +x /app/backend/entrypoint.sh

ENTRYPOINT ["/app/backend/entrypoint.sh"]