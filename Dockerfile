FROM python:3.11

WORKDIR /app

RUN pip install --no-cache-dir poetry gunicorn

COPY pyproject.toml ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root --no-dev

COPY . .

RUN poetry install --no-interaction --no-ansi --no-dev

CMD gunicorn -b :8080 --workers 1 --threads 8 "gptancial:app"
