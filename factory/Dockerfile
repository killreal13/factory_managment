FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
WORKDIR /factory
COPY requirements.txt /factory/
RUN pip install -r requirements.txt
COPY . /factory/