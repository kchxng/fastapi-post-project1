FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt /requirements.txt

ADD ./app .

RUN pip install -r /requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:application", "--reload", "--host", "0.0.0.0", "--port", "8000"]