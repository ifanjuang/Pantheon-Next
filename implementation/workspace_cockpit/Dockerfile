ARG HERMES_IMAGE=nousresearch/hermes-agent:v2026.9.7
FROM ${HERMES_IMAGE}

WORKDIR /app
COPY server.py /app/server.py
COPY static /app/static

ENTRYPOINT ["python3", "/app/server.py"]
CMD ["--host", "0.0.0.0", "--port", "8189", "--max-depth", "2", "--root", "IFJA=/vaults/ifja", "--root", "Affaires=/vaults/affaires", "--root", "Documentaires=/vaults/documentaires"]
