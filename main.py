from pathlib import Path
import sys


def main() -> int:
    entry = Path(__file__).resolve().parent / "entry.txt"
    print(entry.read_text(encoding="utf-8"), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
