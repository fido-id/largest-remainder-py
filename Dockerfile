FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl git build-essential pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Install uv as root, then copy the binary to /usr/local/bin
RUN curl -fsSL https://astral.sh/uv/install.sh | sh && \
    install -m 0755 /root/.local/bin/uv /usr/local/bin/uv

# Create non-root user with same UID as host user
ARG USER_ID=1000
ARG GROUP_ID=1000
RUN groupadd -g ${GROUP_ID} devuser && \
    useradd -m -u ${USER_ID} -g devuser devuser

USER devuser
WORKDIR /workspace

COPY --chown=devuser:devuser . .
RUN uv sync --all-extras --dev --frozen

CMD ["bash"]