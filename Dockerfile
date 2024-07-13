FROM python:3.11-slim-buster

WORKDIR /app

RUN apt-get -y update
RUN apt-get -y install git

COPY requirements.txt .
COPY requirements_dev.txt .

RUN pip install --no-cache-dir -r requirements_dev.txt

COPY . .

EXPOSE 3000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000", "--reload"]