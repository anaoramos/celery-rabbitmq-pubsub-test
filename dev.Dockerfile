# Use a base image with the necessary dependencies
FROM python:3.8-slim-bullseye AS builder

RUN apt update && apt install -y build-essential libcurl4-openssl-dev libssl-dev curl

RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.2.2 python3 -

ADD pyproject.toml poetry.lock /usr/src/

WORKDIR /usr/src

RUN /root/.local/bin/poetry config virtualenvs.in-project true
RUN /root/.local/bin/poetry install --no-root


FROM docker.io/python:3.8-slim-bullseye AS runtime

WORKDIR /usr/src

ENV SITE_DIR=/usr/src

# Install Uvicorn and FastAPI dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy python virtual environment
COPY --from=builder /usr/src/.venv/ $SITE_DIR/.venv/

WORKDIR ${SITE_DIR}/app
COPY . .

VOLUME ${SITE_DIR}/app

CMD $SITE_DIR/.venv/bin/uvicorn app.api.main:app --host 0.0.0.0 --port 8000
