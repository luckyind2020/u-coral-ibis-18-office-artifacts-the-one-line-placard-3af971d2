"""Museum placard for an ordinary office object, treated as an ancient artifact.

Reads the one-line placard from entry.txt (resolved next to this script),
prints it to stdout, and writes it to /output/entry.txt when /output exists.
"""

from pathlib import Path


def load_entry() -> str:
    entry_path = Path(__file__).with_name("entry.txt")
    return entry_path.read_text(encoding="utf-8").strip()


def validate_entry(line: str) -> str:
    """Enforce the bounty limits: exactly one non-empty line, max 180 chars."""
    if not line or not line.strip():
        raise ValueError("entry.txt must not be empty")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 180:
        raise ValueError(f"entry is {len(line)} chars, over the 180-char limit")
    return line


def write_output(line: str) -> None:
    """Write the placard to /output/entry.txt when the grader's /output exists."""
    output_dir = Path("/output")
    if output_dir.is_dir():
        (output_dir / "entry.txt").write_text(line + "\n", encoding="utf-8")


def main() -> None:
    line = validate_entry(load_entry())
    print(line)
    write_output(line)


if __name__ == "__main__":
    main()
