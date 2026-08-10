"""A minimal key=value config parser."""


def load_config(text: str) -> dict[str, str]:
    """Parse ``key=value`` lines into a dict.

    Lines are split on the first ``=``; whitespace around keys and values is
    stripped.
    """
    entries: dict[str, str] = {}
    for line in text.splitlines():
        key, value = line.split("=", 1)
        entries[key.strip()] = value.strip()
    return entries
