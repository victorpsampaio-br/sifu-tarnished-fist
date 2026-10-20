#!/usr/bin/env python3
"""Basic design-data preflight; this does not build or test a game mod."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_FILES = [
    "project.json",
    "abilities.json",
    "characters.json",
    "moves.json",
    "systems.json",
    "preflight.json",
]
BLOCKING_WORDS = ("TODO", "unverified", "blocked", "placeholder")


def main() -> int:
    problems = []
    for filename in DATA_FILES:
        path = ROOT / filename
        if not path.exists():
            problems.append(f"Missing required file: {filename}")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            problems.append(f"{filename}: {exc}")
            continue
        rendered = json.dumps(data, ensure_ascii=False).lower()
        for word in BLOCKING_WORDS:
            if word.lower() in rendered:
                problems.append(f"{filename}: contains unresolved marker '{word}'")

    if problems:
        print("PREFLIGHT BLOCKED — this is a design scaffold, not a playable mod.")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("Preflight data checks passed. This does not prove game compatibility or playability.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
