"""Find the model locally, or download it from a (private) Hugging Face repo.

Model weights are never stored in git. Configure with env vars:
  PII_MODEL_DIR   local folder (default models/tagger-piiranha)
  PII_MODEL_REPO  Hugging Face repo id to download from when the folder is missing
  HF_TOKEN        token with read access (needed for a private repo)
Only the files the ONNX service needs are downloaded (~1.1 GB).
"""
import os
from pathlib import Path

SERVE_FILES = ["onnx/model.onnx", "config.json", "tokenizer.json", "tokenizer_config.json",
               "special_tokens_map.json", "spm.model", "added_tokens.json"]


def ensure_model(path: str | None = None) -> str:
    path = Path(path or os.environ.get("PII_MODEL_DIR", "models/tagger-piiranha"))
    if (path / "onnx" / "model.onnx").exists():
        return str(path)
    repo = os.environ.get("PII_MODEL_REPO")
    if not repo:
        raise FileNotFoundError(f"no model at {path}; set PII_MODEL_REPO (+ HF_TOKEN) to download it")
    from huggingface_hub import snapshot_download
    snapshot_download(repo_id=repo, local_dir=str(path), allow_patterns=SERVE_FILES,
                      token=os.environ.get("HF_TOKEN"))
    return str(path)
