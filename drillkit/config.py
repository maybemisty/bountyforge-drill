"""A minimal key=value config parser."""


def load_config(text: str) -> dict[str, str]:
    """Parse ``key=value`` lines into a dict.

    Lines are split on the first ``=``; whitespace around keys and values is
    stripped. Blank lines and lines whose first non-space character is ``#``
    are ignored.

    Raises:
        ValueError: if a line is neither blank, a comment, nor ``key=value``.
    """
    entries: dict[str, str] = {}
    for number, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if "=" not in stripped:
            raise ValueError(
                f"line {number}: expected 'key=value', got {stripped!r}"
            )
        key, value = stripped.split("=", 1)
        entries[key.strip()] = value.strip()
    return entries
