# MyAIShortCut

MY AI Shortcut — myaishortcut.site

This repository is a **Hermes Agent profile distribution**. A buyer installs it
and gets the DBRA agent: persona, skills, routines, and a plain-English guide.

## Layout

- `distribution.yaml` — the profile manifest (name, version).
- `SOUL.md` — the agent's persona.
- `skills/one-shot-tasks/` — the one-shot (local Code Mode) skill.
- `cron/jobs.json` — starter routines (install paused; resume after review).
- `guide/getting-started.md` — the buyer's setup guide.
- `.env.EXAMPLE` — template for a bring-your-own model key.
- `site/` — the marketing website source (not part of the profile). The Worker also
  serves `/shortcut` (Shortcut of the Week), derived from the same template.
- `starter-site/` — a complete first website (4 pages + CSS + JS) that buyers can
  clone, rebrand, and publish. Plain HTML, no build step.
  See `starter-site/README.md`.

## Install (buyer)

```
hermes profile install github.com/alexdurig/MyAIShortCut
hermes -p my-ai-shortcut chat
```
