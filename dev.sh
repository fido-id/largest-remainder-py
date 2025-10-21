#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="largest-remainder-dev"
CONTAINER_NAME="largest-remainder-container"
WORKDIR="/workspace"

echo "🚀 Building Docker image: ${IMAGE_NAME}"
if ! docker build -t "${IMAGE_NAME}" .; then
    echo "❌ Docker build failed"
    exit 1
fi

# Check if container already exists
if docker ps -a --format '{{.Names}}' | grep -Eq "^${CONTAINER_NAME}$"; then
    echo "🧹 Removing old container ${CONTAINER_NAME}..."
    docker rm -f "${CONTAINER_NAME}" >/dev/null 2>&1 || true
fi

RUN_COMMAND=$(cat <<'RUN_EOF'
set -euo pipefail
uv sync --all-extras --dev --frozen
pip install -e .
uv run ruff check .
uv run ruff format --check .
uv run mypy
uv run pytest
bash
RUN_EOF
)

echo "🐳 Running development container..."
docker run -it \
    --name "${CONTAINER_NAME}" \
    -v "$(pwd):${WORKDIR}" \
    -w "${WORKDIR}" \
    --rm \
    "${IMAGE_NAME}" \
    bash -lc "${RUN_COMMAND}"
