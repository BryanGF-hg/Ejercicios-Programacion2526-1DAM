#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import json
import textwrap
import time
import sys
import shutil
from datetime import timedelta

MODEL = "qwen2.5:3b-instruct"
INPUT_TXT = "convertido.txt"
OUTPUT_JSONL = "entrenamiento.jsonl"

CHUNK_SIZE = 1200  # characters (approx)
WRAP_BREAK_LONG_WORDS = False
WRAP_DROP_WHITESPACE = True

# Optional: save bad outputs for later inspection
BAD_OUTPUTS_FILE = "entrenamiento.bad.txt"

# Console behavior
SHOW_LAST_QA_PREVIEW = True   # show a short preview of last Q/A
PROGRESS_BAR_WIDTH = 28


def call_ollama(prompt: str) -> tuple[str, str, int, float]:
    """
    Returns: (stdout, stderr, returncode, elapsed_seconds)
    """
    t0 = time.time()
    p = subprocess.run(
        ["ollama", "run", MODEL],
        input=prompt,
        text=True,
        capture_output=True
    )
    dt = time.time() - t0
    return (p.stdout.strip(), (p.stderr or "").strip(), p.returncode, dt)


def human_rate(n: float, unit: str = "it/s") -> str:
    return f"{n:.2f} {unit}"


def fmt_td(seconds: float) -> str:
    if seconds < 0:
        seconds = 0
    return str(timedelta(seconds=int(seconds)))


def term_width(default: int = 100) -> int:
    try:
        return shutil.get_terminal_size((default, 20)).columns
    except Exception:
        return default


def bar(progress: float, width: int) -> str:
    progress = max(0.0, min(1.0, progress))
    filled = int(round(progress * width))
    return "█" * filled + "░" * (width - filled)


def safe_preview(s: str, max_len: int = 140) -> str:
    s = " ".join((s or "").split())
    if len(s) <= max_len:
        return s
    return s[: max_len - 1] + "…"


def print_header(total_chars: int, total_chunks: int) -> None:
    w = term_width()
    title = "Q/A JSONL GENERATOR (Ollama)"
    line = "─" * min(w, 120)

    print(line)
    print(title)
    print(line)
    print(f"Model:        {MODEL}")
    print(f"Input:        {INPUT_TXT}  ({total_chars:,} chars)")
    print(f"Output:       {OUTPUT_JSONL}")
    print(f"Bad outputs:  {BAD_OUTPUTS_FILE} (only invalid JSON)")
    print(f"Chunk size:   {CHUNK_SIZE} chars")
    print(f"Chunks:       {total_chunks}")
    print(line)
    sys.stdout.flush()


def render_stats(
    idx: int,
    total: int,
    ok: int,
    bad: int,
    elapsed: float,
    last_dt: float,
    last_chunk_len: int,
    last_q: str | None,
    last_a: str | None,
    ema_s_per_item: float | None,
) -> None:
    # Rates
    it_done = idx
    it_left = total - it_done
    rate_avg = (it_done / elapsed) if elapsed > 0 else 0.0

    if ema_s_per_item is not None and ema_s_per_item > 0:
        eta = it_left * ema_s_per_item
    else:
        eta = (it_left / rate_avg) if rate_avg > 0 else 0.0

    pct = (it_done / total) if total else 1.0
    w = term_width()
    line = "─" * min(w, 120)

    # Single "rich" block
    print(line)
    print(
        f"[{bar(pct, PROGRESS_BAR_WIDTH)}] "
        f"{it_done}/{total} ({pct*100:5.1f}%)  "
        f"OK:{ok}  BAD:{bad}"
    )
    print(
        f"Elapsed: {fmt_td(elapsed)}  "
        f"ETA: {fmt_td(eta)}  "
        f"Avg: {human_rate(rate_avg)}  "
        f"Last: {last_dt:.2f}s"
    )
    print(f"Last chunk: {last_chunk_len} chars")

    if SHOW_LAST_QA_PREVIEW and last_q is not None and last_a is not None:
        print(f"Q: {safe_preview(last_q)}")
        print(f"A: {safe_preview(last_a)}")

    sys.stdout.flush()


def main():
    # Read input
    with open(INPUT_TXT, "r", encoding="utf-8") as f:
        text = f.read()

    # Chunking
    chunks = textwrap.wrap(
        text,
        CHUNK_SIZE,
        break_long_words=WRAP_BREAK_LONG_WORDS,
        drop_whitespace=WRAP_DROP_WHITESPACE,
        replace_whitespace=True,
    )

    total_chars = len(text)
    total_chunks = len(chunks)

    if total_chunks == 0:
        print("No text / no chunks to process.")
        return

    print_header(total_chars, total_chunks)

    # Stats
    t0 = time.time()
    ok = 0
    bad = 0
    total_ollama_time = 0.0
    min_dt = None
    max_dt = None

    # EMA for ETA stability
    ema_s_per_item = None
    alpha = 0.18  # smoothing factor

    # Prepare bad outputs log
    bad_out = open(BAD_OUTPUTS_FILE, "w", encoding="utf-8")

    last_q = None
    last_a = None

    # Open output JSONL (overwrite)
    with open(OUTPUT_JSONL, "w", encoding="utf-8") as out:
        for i, chunk in enumerate(chunks, start=1):
            prompt = f"""
Estas elaborando preguntas y respuestas sobre ciclos formativos.
Procesa el texto y genera UNA sola pregunta y UNA sola respuesta.
Responde siempre en español.
Devuelve JSON ESTRICTO SOLO con este formato:
{{"question":"...","answer":"..."}}

Text:
\"\"\"
{chunk}
\"\"\"
""".strip()

            stdout, stderr, rc, dt = call_ollama(prompt)
            total_ollama_time += dt

            if min_dt is None or dt < min_dt:
                min_dt = dt
            if max_dt is None or dt > max_dt:
                max_dt = dt

            # Update EMA
            if ema_s_per_item is None:
                ema_s_per_item = dt
            else:
                ema_s_per_item = alpha * dt + (1 - alpha) * ema_s_per_item

            # Parse model output
            parsed = None
            parse_err = None
            try:
                parsed = json.loads(stdout)
                # strict shape
                if not isinstance(parsed, dict) or "question" not in parsed or "answer" not in parsed:
                    raise ValueError("JSON is not an object with keys 'question' and 'answer'")
                if not isinstance(parsed["question"], str) or not isinstance(parsed["answer"], str):
                    raise ValueError("'question' and 'answer' must be strings")
            except Exception as e:
                parse_err = str(e)

            if rc != 0 or parsed is None:
                bad += 1
                # Save diagnostics
                bad_out.write("========================================\n")
                bad_out.write(f"Chunk #{i}/{total_chunks}  len={len(chunk)}  rc={rc}  dt={dt:.2f}s\n")
                if stderr:
                    bad_out.write("---- STDERR ----\n")
                    bad_out.write(stderr + "\n")
                bad_out.write("---- STDOUT ----\n")
                bad_out.write(stdout + "\n")
                if parse_err:
                    bad_out.write("---- PARSE ERROR ----\n")
                    bad_out.write(parse_err + "\n")
                bad_out.write("\n")
                bad_out.flush()

                # Print a compact warning line (and keep going)
                elapsed = time.time() - t0
                render_stats(
                    idx=i,
                    total=total_chunks,
                    ok=ok,
                    bad=bad,
                    elapsed=elapsed,
                    last_dt=dt,
                    last_chunk_len=len(chunk),
                    last_q=last_q,
                    last_a=last_a,
                    ema_s_per_item=ema_s_per_item,
                )
                print("⚠️ Skipped invalid model output (see entrenamiento.bad.txt)")
                continue

            # Write JSONL
            out.write(json.dumps(parsed, ensure_ascii=False) + "\n")
            out.flush()
            ok += 1

            last_q = parsed.get("question")
            last_a = parsed.get("answer")

            # Render stats each iteration (rich console)
            elapsed = time.time() - t0
            render_stats(
                idx=i,
                total=total_chunks,
                ok=ok,
                bad=bad,
                elapsed=elapsed,
                last_dt=dt,
                last_chunk_len=len(chunk),
                last_q=last_q,
                last_a=last_a,
                ema_s_per_item=ema_s_per_item,
            )

    bad_out.close()

    # Final summary
    elapsed = time.time() - t0
    avg_dt = (total_ollama_time / total_chunks) if total_chunks else 0.0
    rate = (total_chunks / elapsed) if elapsed > 0 else 0.0
    success_rate = (ok / total_chunks * 100.0) if total_chunks else 0.0

    w = term_width()
    line = "═" * min(w, 120)
    print(line)
    print("DONE")
    print(line)
    print(f"Chunks total:     {total_chunks}")
    print(f"Valid written:    {ok}")
    print(f"Invalid skipped:  {bad}")
    print(f"Success rate:     {success_rate:.1f}%")
    print(f"Total elapsed:    {fmt_td(elapsed)}")
    print(f"Ollama avg/chunk: {avg_dt:.2f}s   (min {min_dt:.2f}s, max {max_dt:.2f}s)")
    print(f"Throughput:       {rate:.2f} chunks/s")
    print(f"Output file:      {OUTPUT_JSONL}")
    if bad:
        print(f"Invalid details:  {BAD_OUTPUTS_FILE}")
    print(line)


if __name__ == "__main__":
    main()

