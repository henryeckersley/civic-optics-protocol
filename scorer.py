#!/usr/bin/env python3
"""
Civic Optics Protocol scorer

This script calculates the Civic Optics Index (COI) given scores for the five criteria.
You can run it interactively or provide the scores as command‑line arguments.

Example usage:

    python3 scorer.py 8 7 8 8 9

This would produce a COI of 7.85 (78.5/100).
"""
import sys
from typing import List

WEIGHTS = [0.20, 0.30, 0.20, 0.15, 0.15]

CRITERIA = [
    "Legibility",
    "Understandability",
    "Navigability",
    "Currency",
    "Actionability",
]

def compute_coi(scores: List[float]) -> float:
    return sum(w * s for w, s in zip(WEIGHTS, scores))

def main():
    args = sys.argv[1:]
    if args:
        if len(args) != 5:
            print("Please provide exactly five scores (0–10) for L, U, N, C, A.")
            sys.exit(1)
        scores = [float(x) for x in args]
    else:
        scores = []
        for criterion in CRITERIA:
            while True:
                try:
                    val = float(input(f"Enter {criterion} score (0–10): "))
                except ValueError:
                    print("Invalid number.  Try again.")
                    continue
                if 0 <= val <= 10:
                    scores.append(val)
                    break
                else:
                    print("Score must be between 0 and 10.")
    coi = compute_coi(scores)
    print(f"COI: {coi:.2f} (out of 10) or {coi * 10:.1f}/100")

if __name__ == "__main__":
    main()
