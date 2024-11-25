FROM debian:bookworm-slim AS builder

# ENV CARGO_HOME="/opt/.cargo"

SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

WORKDIR /opt

# The installer requires curl (and certificates) to download the release archive
# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates curl

# Run uv installer
RUN curl -LsSf https://astral.sh/uv/install.sh | sh


FROM mcr.microsoft.com/vscode/devcontainers/base:bookworm


ENV CARGO_HOME="/opt/.cargo"
ENV PATH="$CARGO_HOME/:$PATH"
ENV PYTHONUNBUFFERED=True
ENV UV_LINK_MODE=copy

WORKDIR /opt

COPY --from=builder --chown=vscode: /root/.local/bin $CARGO_HOME

# install gcloud command
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg \
    && apt-get update -y \
    && apt-get install google-cloud-sdk golang -y

