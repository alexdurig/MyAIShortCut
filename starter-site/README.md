# Your First Website — Starter Kit

A complete, working small-business website: four pages, one stylesheet, one small
script. **Plain HTML, CSS and JavaScript. No build step, no package manager, no
framework.** If you can open a folder, you can run this.

It is set up as a bookkeeping business ("Bluebird Bookkeeping") so every page reads
like a real site instead of a wall of placeholders. Change the words and the colors
and it becomes *your* site.

---

## What's inside

| File | What it is |
|---|---|
| `index.html` | Home page — hero, three services, why-choose-us, testimonial, call to action |
| `services.html` | Services and pricing — three packages |
| `about.html` | About page — your story, how you work, an owner card |
| `contact.html` | Contact page — form plus direct details |
| `styles.css` | All the styling. **Rebrand the whole site by editing six colors at the top.** |
| `script.js` | Two small behaviors: mobile menu, current year in the footer |

## Look at it on your own computer

Open `index.html` in any browser — it just works.

Or serve the folder so the address looks like a real site:

```sh
python3 -m http.server 8000
```

Then visit <http://localhost:8000>.

## Make it yours — five edits

Search the files for the word **EDIT**. That's every place that needs your touch:

1. **Business name** — appears in the header, footer and page titles.
2. **Colors** — open `styles.css`, edit the six values under `:root`. Done.
3. **Your story and services** — replace the sample copy on each page.
4. **Contact details** — email, phone, hours in the footer and on `contact.html`.
5. **Photo** — drop your own image into this folder and point the owner card at it
   (or delete the owner card).

The contact form uses [Formspree](https://formspree.io) (free tier) as a placeholder.
Replace `YOUR_FORM_ID` in `contact.html` with your own endpoint, or delete the form.

## Put it on the internet — free

Any static host works. Easiest free options:

- **Cloudflare Pages** — drag the folder onto the dashboard, or connect the repo.
- **GitHub Pages** — push this folder to a repository and enable Pages in settings.
- **Netlify** — drag and drop the folder.

Keep `index.html` at the root of what you publish.

## Good next steps

- Add your real logo (replace the text brand in the header).
- Write one more page about whatever makes you different.
- Add a separate privacy policy page if you collect emails.

---

Part of **MY AI Shortcut**. Questions? See `guide/getting-started.md` in this repository.
