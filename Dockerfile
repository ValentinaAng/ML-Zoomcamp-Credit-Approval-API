FROM python:3.12-slim-bookworm

# Install poetry
RUN pip install poetry==1.8.4

# Create working directory inside the container
WORKDIR /app

# Copy required files
COPY pyproject.toml poetry.lock /app/

# Install dependencies
RUN poetry install --no-dev --verbose

# Copy the rest of the code
COPY /app /app

# Expose port
EXPOSE 8000

# Run the application
CMD ["poetry", "run", "uvicorn", "main:app", "--reload"]