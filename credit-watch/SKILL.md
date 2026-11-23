---
name: credit-watch
description: "Use when asked about AI credit use, spend, or limits; before big jobs."
metadata:
  hermes:
    tags: [nous, portal, credits, usage, budget, guardrail]
    related_skills: [nous-budget-reporting]
---

# Credit watch

Keeps an eye on this machine's Nous Portal usage so nobody gets a surprise bill.

## When to use

- The user asks what they are spending, how much credit is left, or whether they
  are close to a limit.
- **Before a big job** — long research, bulk generation, anything that will burn
  through many credits. Check first, then say what it may cost and ask before
  running it.
- On the weekly credit-watch routine.

## How

```
/opt/hermes/.venv/bin/python3 <profile>/credit-watch/scripts/check_usage.py
```

Read the output and relay it in plain words. Short is fine:

> Plus plan, $20 a month, renews Dec 13. You've used 4% this month. Auto top-up
> is off, so nothing extra can be charged without you asking.

If any gauge is at or above **80%**, say so clearly and suggest waiting for the
reset, or topping up deliberately.

## Rules

- **Never estimate.** If the portal cannot be reached, say that — do not guess a
  number from memory.
- **Never print tokens**, and never read `auth.json` into the reply. The script
  handles the sign-in; you only see its summary.
- **Do not change account settings unasked.** Turning auto top-up off, raising a
  cap or buying credit are the user's decisions. Recommend, then wait.
- **Free models draw on nothing.** The gauges measure the paid-model allowance.
  Say so — it is why most people's spend stays near zero.
- **Keep credit buckets separate:** subscription credits and purchased credits
  are different. Never merge them or "correct" one with the other.
- **A dollar ceiling is not always published.** If the portal reports no spend
  cap, say the percentage and note the dollar figure simply isn't available.
