#!/usr/bin/env bash

MODEL="models/Qwen3-8B-Q4_K_M.gguf"
DRAFT="models/Qwen3-1.7B-Q4_K_M.gguf"
PROMPT="Explain speculative decoding in simple terms"

CTX_SIZES=(2048 4096 8192 16384 32768)
RUNS=3
N_TOKENS=256
OUTFILE="spec_benchmark.csv"

echo "ctx,run,tokens_per_sec,accept_rate,n_predict,n_accept,n_drafted,total_time_ms" > "$OUTFILE"

for CTX in "${CTX_SIZES[@]}"; do
  for i in $(seq 1 $RUNS); do

    echo "Running ctx=$CTX run=$i"

    LOGFILE="tmp.log"

    ./build/bin/llama-speculative \
      -m "$MODEL" \
      -md "$DRAFT" \
      -c "$CTX" \
      -p "$PROMPT" \
      -n "$N_TOKENS" \
      --spec-draft-n-max 4 \
      > "$LOGFILE" 2>&1

    read TPS ACC NPRED NAC NDR TTIME <<< $(python3 parse_log.py "$LOGFILE")

    echo "$CTX,$i,$TPS,$ACC,$NPRED,$NAC,$NDR,$TTIME" >> "$OUTFILE"

  done
done

echo "Done → $OUTFILE"
