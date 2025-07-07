# Use official Python slim image
FROM python:3.13-slim

# Install uv from the official container
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set workdir
WORKDIR /app

# Copy only the lock and pyproject first, for layer caching
COPY pyproject.toml ./
COPY uv.lock ./

# Install Python deps into system
RUN uv pip install --system --no-cache --editable .

# Copy the rest of your app
COPY . .

# Expose port
EXPOSE 8000

# Run the app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--reload-dir", "app"]
