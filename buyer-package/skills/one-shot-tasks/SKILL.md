---
name: one-shot-tasks
description: "Use when a job needs several steps. Write and run one script that does the whole job, then report only the result."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [code-mode, one-shot, scripting, workflow, efficiency, tool-use, batch]
    related_skills: [test-driven-development, systematic-debugging]
---

# One-shot tasks (the local Code Mode pattern)

## The idea
When a job needs several steps, do not do it one tool call at a time. Write **one
script** that does the whole job, run it, and report only the final result.

One script is one round trip. Many tool calls are many round trips — each one
costs time, tokens, and attention, and every intermediate result sits in the
context.

## When to use
- The job has 3+ steps, or needs a loop or a branch.
- You are about to make several dependent tool calls.
- The intermediate data is large but the final answer is small.
- You are working through a list or a batch.

## When NOT to use
- One tool call answers it — just call it.
- The step is irreversible (delete, send, publish, spend, share) — do it directly
  and confirm with the user first; never bury it in a script.
- The job needs human judgment at each step.
- The user wants to watch each step happen.

## How
1. **Plan** the steps in plain language.
2. **Write one script.** Python via `execute_code` for data work; a shell script
   via `terminal` for files and system work. Keep it short.
3. **Run it.**
4. **Report only the result** — the final answer, plus any errors that need a
   decision. Do not paste the whole intermediate output.

## Rules
- **Safe by default.** A one-shot script must not delete, send, publish, spend, or
  share anything. If the job needs one of those, stop and confirm first.
- **Handle failure.** If a step can fail, catch it in the script and report which
  items failed.
- **Free first.** No paid tools or services.
- **Show your work.** If the user asks, show the script.
- **Don't over-script.** Two calls? Just make two calls.

## Example
User: "Here is a CSV of 500 invoices. Total the amount due by customer."

```python
import csv, collections
totals = collections.defaultdict(float)
with open("invoices.csv", newline="") as f:
    for row in csv.DictReader(f):
        try:
            totals[row["customer"]] += float(row["amount_due"])
        except (KeyError, ValueError):
            continue
for customer, total in sorted(totals.items(), key=lambda x: -x[1]):
    print(f"{customer:30} ${total:,.2f}")
```

Report: a short table of customer totals, plus "3 rows skipped (bad amount)."

## Why it works
Models write code better than they chain tool calls. One script keeps the
intermediate data out of the context and finishes the job in a single pass.
This is the same idea as Cloudflare's "Code Mode" — the local, free version.
