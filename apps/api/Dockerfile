FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml ./
RUN pip install -U pip && pip install -e .
COPY src ./src
ENV PORT=8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
