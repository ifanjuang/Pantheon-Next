FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml README.md ./
COPY pantheon_app ./pantheon_app
COPY openwebui ./openwebui

RUN python -m pip install --no-cache-dir ".[cockpit]" \
    && useradd --create-home --uid 10001 pantheon

USER pantheon

EXPOSE 8081

CMD ["pantheon-cockpit"]
