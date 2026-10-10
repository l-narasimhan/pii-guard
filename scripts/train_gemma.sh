#!/bin/zsh
# Gemma-4 E2B LoRA stage only (tagger already trained + evaluated).
cd "$(dirname "$0")/.."
LOG=reports/m3_train.log
export PYTHONUNBUFFERED=1 NO_COLOR=1
echo "[$(date +%T)] TRAIN Gemma-4 E2B LoRA (QLoRA, 2000 iters) — progress rows: iter / train_loss / tok/s" >> $LOG
.venv/bin/python -m mlx_lm lora --model mlx-community/gemma-4-e2b-it-4bit --train --data data/sft \
  --adapter-path models/gemma-e2b-lora --iters 2000 --batch-size 4 --num-layers 16 --learning-rate 1e-4 \
  --mask-prompt --grad-checkpoint --steps-per-eval 250 --val-batches 25 --steps-per-report 50 --save-every 500 \
  --max-seq-length 512 2>&1 | sed -u 's/\x1b\[[0-9;]*m//g' | grep --line-buffered -E '^ +[0-9]+ |Error|error|Traceback' >> $LOG
echo "[$(date +%T)] EVAL Gemma E2B LoRA" >> $LOG
.venv/bin/python -m pii.gemma mlx-community/gemma-4-e2b-it-4bit data/handwritten.jsonl data/test.jsonl \
  --adapter models/gemma-e2b-lora 2>&1 | grep --line-buffered -E '^(===|\| \*\*|\*\*PII|\*\*Latency|\| NAME|\| ADDRESS|\| PHONE|stats)' >> $LOG
echo "[$(date +%T)] ALL DONE" >> $LOG
