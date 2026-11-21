# MY AI Shortcut — buyer package

This folder is what a buyer receives: a Hermes Agent **profile distribution**.
Drop it into Hermes and the agent is installed as its own profile.

## What's inside

- `skills/one-shot-tasks/` — the one-shot skill (the local Code Mode pattern).
  For any multi-step job, the agent writes one script, runs it, and reports the
  result — instead of calling tools one at a time.
- `guide/getting-started.md` — the plain-English setup guide.
- `routines/` — standing routines (coming).
- `persona/`, `config/` — persona and configuration (coming).

## Install

```
hermes profile install <this repository>
hermes -p my-ai-shortcut chat
```

You'll be asked to sign in to the private repository the first time.

## Keep it up to date

```
hermes profile update my-ai-shortcut
```

Your memories, sessions, and settings are kept.

## Never included

Memories, sessions, and credentials are never part of this package. If you see
any, contact us before using them.
