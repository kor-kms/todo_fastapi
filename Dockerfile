FROM python:3.11.3 as requirements-stage
WORKDIR /workspace
RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /workspace/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11.3
WORKDIR /code
COPY --from=requirements-stage /workspace/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
