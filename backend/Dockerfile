FROM python:3.8

WORKDIR /app

COPY ../ /app

RUN python -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt --no-cache-dir
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]