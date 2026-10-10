# PII Guard: India-first PII redaction service (rules + ONNX tagger), CPU only.
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 \
    PII_HOST=0.0.0.0 PII_PORT=5240 PII_MODE=prod \
    PII_MODEL_DIR=/app/models/tagger HF_HOME=/tmp/hf

WORKDIR /app
COPY requirements-serve.txt .
RUN pip install --no-cache-dir -r requirements-serve.txt

COPY pii/ pii/

# Model weights are not baked into the image (licence + size). At start-up the service
# looks in PII_MODEL_DIR (mount a volume there) or downloads PII_MODEL_REPO using HF_TOKEN.
RUN useradd --create-home --uid 10001 pii && mkdir -p /app/models && chown -R pii /app
USER pii

EXPOSE 5240
HEALTHCHECK --interval=30s --timeout=5s --start-period=120s --retries=3 \
  CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:5240/health',timeout=4).status==200 else 1)"

CMD ["python", "-m", "pii.server"]
