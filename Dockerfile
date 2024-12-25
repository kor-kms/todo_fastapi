FROM python:3.11.3 as requirements-stage
WORKDIR /code/workspace
RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /code/workspace/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

RUN pip install --no-cache-dir --upgrade -r /code/workspace/requirements.txt

COPY . /code/workspace
