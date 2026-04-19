# Civic Optics Protocol (COP‑1)

The **Civic Optics Protocol** is an open standard for assessing the quality of public‑facing civic information.  The goal is to ensure that important government‑issued materials—such as absentee voting instructions, policy guides or meeting notices—are **legible**, **understandable**, **navigable**, **current** and **actionable**.

This repository contains the core standard (`protocol.md`), a simple Python scoring script (`scorer.py`), a minimal static website (`index.html`) and a few sample audits demonstrating how COP‑1 can be applied in practice.

## Files

| File | Description |
| --- | --- |
| `protocol.md` | Detailed description of the COP‑1 criteria and scoring weights. |
| `scorer.py` | Example script that calculates a weighted Civic Optics Index given scores for each criterion. |
| `index.html` | Simple microsite that describes the project and links to audits. |
| `audits/sample_audit.md` | Sample audit covering three Georgia absentee‑voting pages. |

## Usage

1. Read `protocol.md` to understand the scoring rubric.
2. Use the `scorer.py` script to compute a weighted score.  You can run it with Python 3 and pass scores via command‑line arguments or modify it to suit your needs.
3. Review the sample audit in `audits/sample_audit.md` for guidance on producing your own audits.
4. Publish your audits publicly to encourage feedback and adoption.

## License

This project is released into the public domain under the Creative Commons Zero (CC0) license.  You are free to use, adapt and redistribute it without restriction.
