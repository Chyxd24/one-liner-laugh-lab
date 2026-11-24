"""One-Liner Laugh Lab entry — writes the single joke line to /output/entry.txt."""

from pathlib import Path

LINE = (
    "I'm not out of ink, I'm on strike: you hit print 47 times today "
    "and not one page deserved it."
)

assert len(LINE) <= 200, f"line too long: {len(LINE)}"

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(LINE + "\n", encoding="utf-8")
print(f"wrote {len(LINE)} chars -> {out}")