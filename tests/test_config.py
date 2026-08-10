import pytest

from drillkit import load_config


def test_parses_a_single_pair():
    assert load_config("retries=3") == {"retries": "3"}


def test_parses_multiple_pairs():
    assert load_config("retries=3\ntimeout=30") == {"retries": "3", "timeout": "30"}


def test_strips_whitespace():
    assert load_config("  retries = 3 ") == {"retries": "3"}


def test_skips_blank_lines():
    assert load_config("retries=3\n\n   \ntimeout=30") == {
        "retries": "3",
        "timeout": "30",
    }


def test_skips_comment_lines():
    assert load_config("# how many times to retry\n  # indented\nretries=3") == {
        "retries": "3"
    }


def test_parses_blank_and_comment_lines_mixed_with_pairs():
    text = "retries=3\n\n# how many times to retry\ntimeout=30"
    assert load_config(text) == {"retries": "3", "timeout": "30"}


def test_malformed_line_reports_the_line_number_and_content():
    with pytest.raises(ValueError) as excinfo:
        load_config("retries=3\nnonsense")

    message = str(excinfo.value)
    assert "line 2" in message
    assert "'nonsense'" in message
    assert "key=value" in message
