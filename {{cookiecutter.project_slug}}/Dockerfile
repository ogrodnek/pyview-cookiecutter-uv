FROM python:3.12-alpine as build

RUN apk add build-base libffi-dev

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen --no-install-project --no-dev

# Copy application code
COPY . .

FROM python:3.12-alpine as runtime

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1

COPY --from=build /app /app

WORKDIR /app/src

CMD [ "uvicorn", "--host",  "0.0.0.0", "--port", "{{ cookiecutter.port }}", "{{ cookiecutter.package_name }}.app:app" ]
