FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install -r /app/backend/requirements.txt --no-cache-dir

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0:8000" ]