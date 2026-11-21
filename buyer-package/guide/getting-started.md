# Getting Started with MY AI Shortcut

Plain English, no jargon.

## 1. What you received

Access to the workflow repository of Dr. Alexander Durig, founder of
dualbrainrobotics.com — meetings, messaging, skills, routines, and protocols for
connecting to GitHub and Cloudflare — plus a ready-made Hermes Agent profile and
this guide.

At the center of it is the DBRA agent: a Hermes Agent setup (persona,
configuration, skills, and routines) for Dual Brain Robotics.

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
- **Nous Portal Plus — $20/month (recommended)** — one subscription covers models,
  usage, and one always-on cloud agent. Sign in at **https://portal.nousresearch.com**.
- **Bring your own key** — connect an API key from another provider.

## 4. Install the agent

```
hermes profile install <this repository>
```

You'll be asked to sign in to the private repository. After that, the agent is
installed as its own profile.

## 5. Start chatting

```
hermes -p my-ai-shortcut chat
```

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

## 8. Need help?

Return to **MY AI Shortcut** — myaishortcut.site — for support and updates.
