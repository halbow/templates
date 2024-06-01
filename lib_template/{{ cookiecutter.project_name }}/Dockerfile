FROM python:3.12 as development
WORKDIR /app

COPY pyproject.toml ./

RUN pip install --upgrade pip
RUN pip install -e .[dev]

