FROM python:3.8-slim

ARG POETRY_VERSION=1.2.2

ENV POETRY_VERSION=${POETRY_VERSION} \
    APP_ROOT=/server

WORKDIR ${APP_ROOT}

RUN pip install "poetry==$POETRY_VERSION"

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi --only main

COPY . ./

RUN INSCRIBE_DEBUG=1 python manage.py collectstatic --noinput

CMD /server/start.sh
