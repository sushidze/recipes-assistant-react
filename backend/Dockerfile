FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt --no-cache-dir

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]