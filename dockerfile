FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app

RUN pip install awscli

RUN pip install -r requierments.txt
CMD ["python3","application.py"]