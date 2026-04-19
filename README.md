# Civic Optics Protocol (COP-1)

This project scores whether a public-facing government page is actually usable.

The live homepage is now a **working calculator**. You do not need Python to use the main tool anymore.

## What this measures

COP-1 scores a page across five categories:

- **Legibility** — can a normal person read it quickly?
- **Understandability** — does it make sense without jargon?
- **Navigability** — can people find what matters fast?
- **Currency** — does it look current and up to date?
- **Actionability** — does it clearly tell people what to do next?

## Fastest way to use it

1. Open the live site homepage.
2. Enter the page name and URL.
3. Move the five sliders from 0 to 10.
4. Read the final score out of 100.
5. Click **Copy report** and paste the result into a doc, spreadsheet, email, or article draft.

## Score interpretation

- **85-100** = excellent
- **70-84** = strong
- **55-69** = usable but flawed
- **Below 55** = hard for the public to use

## Example

If a county absentee voting page feels:

- Legibility: 8
- Understandability: 6
- Navigability: 7
- Currency: 5
- Actionability: 9

Then the tool calculates the weighted COP-1 score automatically.

## Files in this repo

| File | What it is |
| --- | --- |
| `index.html` | The actual browser calculator |
| `protocol.md` | The scoring standard |
| `audits/sample_audit.md` | Example writeup |
| `scorer.py` | Command-line fallback calculator |

## Good use cases

- Compare election-information pages across counties
- Score school board notice pages
- Audit city service or permit pages
- Build a ranked list of which civic pages are easiest or hardest to use

## Notes

This is best used as a **human-scored audit tool**, not an automatic crawler. The point is to make your judgment explicit, consistent, and publishable.

## License

CC0 / public domain.
