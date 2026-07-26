# ============================================================================
# Polaris Terminal - Backend Dockerfile
# ============================================================================

# Base Image
FROM python:3.13-slim

# Python Configuration
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV UV_PROJECT_ENVIRONMENT=/opt/venv

# Working Directory
WORKDIR /app

# Install uv (Official Binary)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy Dependency Files
COPY backend/pyproject.toml backend/uv.lock ./

# Install Project Dependencies
RUN uv sync --frozen --no-dev

# Copy Application Source
COPY backend/ .

ENV PATH="/opt/venv/bin:${PATH}"

# Expose FastAPI Port
EXPOSE 8000

# Start Application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]