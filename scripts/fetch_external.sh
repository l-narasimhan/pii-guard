#!/bin/sh
# Download the independent Indian PII benchmarks used in M3 (not stored in git).
#   Ylemis India-PII Benchmark (CC0)   https://huggingface.co/datasets/Pranshurs/ylemis-india-pii-benchmark
#   Maskara Indian PII (MIT)           https://huggingface.co/datasets/somukandula/maskara-indian-pii-200k
set -e
cd "$(dirname "$0")/.."
mkdir -p data/external
HF=https://huggingface.co/datasets
curl -sSL -o data/external/ylemis.jsonl "$HF/Pranshurs/ylemis-india-pii-benchmark/resolve/main/benchmark.jsonl"
curl -sSL -o data/external/maskara_real.parquet "$HF/somukandula/maskara-indian-pii-200k/resolve/main/data/real_world_eval-00000-of-00001.parquet"
curl -sSL -o data/external/maskara_disjoint.parquet "$HF/somukandula/maskara-indian-pii-200k/resolve/main/data/template_disjoint_eval-00000-of-00001.parquet"
echo "7003719c62f451b68ec68280fbccaca12990718ad9ee7aacbcaba66c4c43f914  data/external/ylemis.jsonl" | shasum -a 256 -c
ls -la data/external
