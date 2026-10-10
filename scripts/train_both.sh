#!/bin/zsh
# Sequential: wait for the Gemma baseline run -> train tagger -> eval -> LoRA Gemma E2B -> eval.
cd "$(dirname "$0")/.."
LOG=reports/m3_train.log
export PYTHONUNBUFFERED=1
echo "[$(date +%T)] waiting for Gemma baseline run to finish" >> $LOG
while pgrep -f "pii.gemma mlx-community" > /dev/null; do sleep 30; done

echo "[$(date +%T)] TRAIN tagger (Piiranha base, full fine-tune, 3 epochs)" >> $LOG
.venv/bin/python -m pii.train --base iiiorg/piiranha-v1-detect-personal-information --out models/tagger-piiranha \
  --epochs 3 --bs 16 --lr 5e-5 2>&1 | grep --line-buffered -E '^(device|step [0-9]+0{2}/|   valid|done)' >> $LOG
echo "[$(date +%T)] EVAL tagger" >> $LOG
.venv/bin/python -m pii.tagger models/tagger-piiranha data/handwritten.jsonl data/test.jsonl 2>&1 \
  | grep --line-buffered -E '^(===|\| \*\*|\*\*PII|\*\*Latency|\| NAME|\| ADDRESS|\| PHONE)' >> $LOG

echo "[$(date +%T)] TRAIN Gemma-4 E2B LoRA (QLoRA on 4-bit base)" >> $LOG
.venv/bin/python -m mlx_lm lora --model mlx-community/gemma-4-e2b-it-4bit --train --data data/sft \
  --adapter-path models/gemma-e2b-lora --iters 2000 --batch-size 4 --num-layers 16 --learning-rate 1e-4 \
  --mask-prompt --grad-checkpoint --steps-per-eval 250 --val-batches 25 --save-every 500 --max-seq-length 512 \
  2>&1 | grep --line-buffered -E '^Iter|Val loss|Saved|Trainable|Error|error' >> $LOG
echo "[$(date +%T)] EVAL Gemma E2B LoRA" >> $LOG
.venv/bin/python -m pii.gemma mlx-community/gemma-4-e2b-it-4bit data/handwritten.jsonl data/test.jsonl \
  --adapter models/gemma-e2b-lora 2>&1 | grep --line-buffered -E '^(===|\| \*\*|\*\*PII|\*\*Latency|\| NAME|\| ADDRESS|\| PHONE|stats)' >> $LOG
echo "[$(date +%T)] ALL DONE" >> $LOG
