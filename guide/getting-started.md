# Getting Started with MY AI Shortcut

Plain English, no jargon.

## 1. What you received

Access to the workflow repository of Dr. Alexander Durig, founder of
dualbrainrobotics.com — meetings, messaging, skills, routines, and protocols for
connecting to GitHub and Cloudflare — plus a ready-made Hermes Agent profile and
this guide.

At the center of it is the DBRA agent: a Hermes Agent setup (persona,
configuration, skills, and routines) for Dual Brain Robotics.

### What's in the box

| Folder | What it is |
|---|---|
| `SOUL.md` | The agent's persona — how it talks and works. |
| `.env.EXAMPLE` | Template for your model connection. No secrets included. |
| `skills/one-shot-tasks/` | The skill that lets the agent run a whole multi-step job in one go. |
| `cron/jobs.json` | Two starter routines (morning brief, weekly review). Ships paused. |
| `guide/getting-started.md` | This guide. |
| `starter-site/` | A complete first website you can make your own. See section 8. |

**One habit makes all of this work.** Whenever you wonder how to do something, ask
your agent. It can read these files, change them, and explain anything in this guide
— and if it cannot do something, it will tell you honestly.

## 2. Install Hermes Agent (free)

Hermes Agent is free and open source (MIT license).

- Download it for Windows, macOS, or Linux at **https://hermes-agent.nousresearch.com**
- or, in a terminal:

  ```
  curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
  ```

Then start it:

```
hermes
```

## 3. Connect a model

Hermes needs a model to think with. You have three options:

- **Free tier** — pay-as-you-go, free models only. Good for trying it out.
- **Plus — $20/month (recommended)** — the Nous Portal plan we recommend: one
  subscription covers models, usage, and one always-on cloud agent. Sign in at
  **https://portal.nousresearch.com**.
- **Bring your own key** — connect an API key from another provider.

**Your agent watches your usage.** Ask it any time what you have used. It reads
your own Nous Portal account, tells you plainly, and flags when you are running
low. Keep auto top-up off and nothing extra can ever be charged without you
asking.

## 4. Install the agent

**First, a free GitHub account.** Go to **https://github.com** and sign up — it
takes about two minutes.

Then run this command:

```
hermes profile install github.com/alexdurig/MyAIShortCut
```

The repository is public, so there is nothing to accept and no waiting: the
agent installs itself as its own profile.

**Or skip the terminal.** Open the same repository in your browser, click the
green **Code** button, then **Download ZIP**.

If the command says it cannot see the repository, try it again.

## 5. Start chatting

```
hermes -p my-ai-shortcut chat
```

The first time, Hermes may ask you to sign in to your Nous account — that is
expected, and it is the same account from step 3. It takes about a minute.

That's it — you're talking to your agent.

## 6. Keep it up to date

When the agent is improved, pull the new version (your own memories and settings
are kept):

```
hermes profile update my-ai-shortcut
```

## 7. A tip for getting the best results

Give it the whole job. Tell it what you want done — it works through the steps
and comes back with the result, not just an answer.

## 8. Build your first website (starter kit included)

Inside `starter-site/` there is a complete small-business website: four pages, one
stylesheet, one small script. There is **no build step** — open `index.html` in a
browser and it works.

It comes pre-filled with a sample business ("Bluebird Bookkeeping") so every page
reads like a real site rather than a blank form.

### Let your agent do the renaming

This is the part buyers love. Ask your agent:

> "Show me every file that mentions Alexander Durig or Bluebird Bookkeeping."

It will list them. Then tell it:

> "Delete the ones I don't want. Keep the ones I like, and change them into my name."

Your agent does the work and shows you what changed.

### Or do it by hand

Search the files for the word **EDIT** — those are the only places that need your own
words:

1. Business name (header, footer, page titles)
2. Colors (six values at the top of `styles.css`)
3. Your story, services, and prices
4. Your email, phone, and hours
5. Your photo

Full walkthrough: `starter-site/README.md`. Publishing is free — Cloudflare Pages,
GitHub Pages, or Netlify all take the folder exactly as it is.

## 9. Need help?

**Ask your agent first.** It can read these files and answer most questions on the
spot — and it is happy to.

**Email us anytime:** [alex@myaishortcut.site](mailto:alex@myaishortcut.site)

And return to **MY AI Shortcut** — myaishortcut.site — for updates.
