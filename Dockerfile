FROM python:3.7.7-slim

RUN pip install aws-sam-cli

WORKDIR /app

ENV SAM_CLI_TELEMETRY=0

COPY sentry-sdk sentry-sdk
COPY template.yaml ./
COPY src src

COPY samconfig.toml ./

ENTRYPOINT sam deploy
