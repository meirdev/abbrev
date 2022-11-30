from abbrev import abbrev


def test_abbrev():
    abbrs = abbrev("apple", "apricot")

    assert abbrs == {
        "app": "apple",
        "appl": "apple",
        "apple": "apple",
        "apr": "apricot",
        "apri": "apricot",
        "apric": "apricot",
        "aprico": "apricot",
        "apricot": "apricot",
    }


def test_abbrev_with_pattern():
    abbrs = abbrev("apple", "apricot", pattern=r".*[eo].*")

    assert abbrs == {
        "apple": "apple",
        "aprico": "apricot",
        "apricot": "apricot",
    }
