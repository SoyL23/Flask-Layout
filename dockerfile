FROM ubuntu:22.04

RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    libpq-dev \
    gcc \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app


RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "-B", "src/main.py"]
