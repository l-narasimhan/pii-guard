"""Upload the trained tagger to a PRIVATE Hugging Face model repo (needs `hf auth login`).

    .venv/bin/python scripts/upload_model.py <your-hf-username>/pii-guard-tagger

Uploads what serving and retraining need (config, tokenizer, safetensors, onnx/model.onnx),
not the rejected int8 file. The model is derived from Piiranha (CC BY-NC-ND 4.0):
personal, non-commercial use only; keep the repo private.
"""
import json
import sys
from pathlib import Path

from huggingface_hub import HfApi

MODEL_DIR = Path("models/tagger-piiranha")
CARD = """---
license: cc-by-nc-nd-4.0
base_model: iiiorg/piiranha-v1-detect-personal-information
tags: [pii, token-classification, india, hinglish, private]
---

# PII Guard tagger (private, personal use)

Token classifier for Indian PII (16 types: NAME, ADDRESS, PHONE, EMAIL, UPI, AADHAAR, PAN, GSTIN,
CARD, BANK_ACCT, PASSPORT, VOTER_ID, VEHICLE, DOB, IP, DL) in English, Hinglish and South Indian
languages written in Latin script. Used with the rules + format checks in
[pii-guard](https://github.com/l-narasimhan/pii-guard).

**Licence:** fine-tuned from `iiiorg/piiranha-v1-detect-personal-information` (CC BY-NC-ND 4.0).
Non-commercial, personal use only; this derivative must not be shared or deployed commercially.
For commercial use, retrain from `microsoft/deberta-v3-base` (MIT) with the repo's `pii.train --base`.

- Training: 15,000 synthetic examples, 3 epochs, full fine-tune; best validation loss {best:.4f}
- Engine leak (PII characters left visible): 0.4–0.6% Ylemis India-PII, 2–5% Maskara, 0.3% own hand-written set
- Files: `model.safetensors` (PyTorch), `onnx/model.onnx` (serving, identical output, ~9 ms on CPU)
"""


def main(repo_id: str):
    log = json.load(open(MODEL_DIR / "train_log.json"))
    (MODEL_DIR / "README.md").write_text(CARD.format(best=log["best_valid_loss"]))
    api = HfApi()
    api.create_repo(repo_id, repo_type="model", private=True, exist_ok=True)
    info = api.repo_info(repo_id)
    assert info.private, f"{repo_id} is not private; refusing to upload a CC BY-NC-ND derivative"
    api.upload_folder(
        repo_id=repo_id, folder_path=str(MODEL_DIR),
        allow_patterns=["README.md", "config.json", "tokenizer*.json", "special_tokens_map.json", "spm.model",
                        "added_tokens.json", "model.safetensors", "train_log.json", "onnx/model.onnx"],
        commit_message="Upload PII Guard tagger (private, personal use)",
    )
    print(f"uploaded -> https://huggingface.co/{repo_id} (private)")


if __name__ == "__main__":
    main(sys.argv[1])
