from drillkit import load_config


def test_parses_a_single_pair():
    assert load_config("retries=3") == {"retries": "3"}


def test_parses_multiple_pairs():
    assert load_config("retries=3\ntimeout=30") == {"retries": "3", "timeout": "30"}


def test_strips_whitespace():
    assert load_config("  retries = 3 ") == {"retries": "3"}
