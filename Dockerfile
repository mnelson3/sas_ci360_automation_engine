FROM python:3.11-slim
LABEL maintainer="support@nelsongrey.com"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/opt/sas_ci360_automation_engine/src

WORKDIR /opt/sas_ci360_automation_engine

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY src ./src
RUN mkdir -p logs data

CMD ["python3", "-m", "main.Main"]
