FROM python:3.12-slim-bookworm

RUN apt-get update

COPY --from=ghcr.io/astral-sh/uv:0.8.2 /uv /uvx /bin/

ADD . /app

# Sync the project into a new environment, asserting the lockfile is up to date
WORKDIR /app
RUN uv sync

RUN uv sync --locked

EXPOSE 8080
CMD ["uv", "run", "main.py"]