# Civic Optics Protocol (COP-1)

This project scores whether a public-facing government page is actually usable.

The homepage is now a **semi-automated analyzer**, not just a manual slider page.

## What the tool now does

You can:

1. Paste a **URL** and let the site try to fetch the page.
2. Or paste the **page text or raw HTML** directly.
3. The analyzer then extracts evidence and suggests scores for:
   - **Legibility**
   - **Understandability**
   - **Navigability**
   - **Currency**
   - **Actionability**
4. You can still override the suggested scores manually.
5. Click **Copy report** to export a writeup.

## What it automatically looks for

The analyzer checks signals like:

- word count
- reading ease
- heading count
- links
- list items
- long paragraphs
- detected dates
- update language
- action words
- contact info
- forms/buttons
- jargon-like terms

## Important limitation

This is a static GitHub Pages site, so direct URL analysis can fail when a website blocks browser cross-origin requests.

When that happens, paste the visible page text or raw HTML into the source box and the analyzer still works.

## Score interpretation

- **85-100** = excellent
- **70-84** = strong
- **55-69** = usable but flawed
- **Below 55** = hard for the public to use

## Files in this repo

| File | What it is |
| --- | --- |
| `index.html` | Semi-automated browser analyzer |
| `protocol.md` | Scoring standard |
| `audit-template.md` | Copyable writeup template |
| `audits/sample_audit.md` | Example audit |
| `scorer.py` | Command-line fallback calculator |

## Good use cases

- compare election-information pages across counties
- score school board notice pages
- audit city service or permit pages
- rank which public pages are easiest or hardest to use

## Notes

This is still a **human-in-the-loop audit tool**, not a full autonomous crawler. The point is to combine extracted evidence with human judgment so the result is more defensible and publishable.

## License

CC0 / public domain.
