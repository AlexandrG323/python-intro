from collections_practice import (
    even_squares,
    flatten,
    top_n,
    total_by_year,
    unique_sorted,
    word_counts,
)


def test_unique_sorted() -> None:
    assert unique_sorted(["cola", "jameson", "cola", "apple"]) == [
        "apple",
        "cola",
        "jameson",
    ]
    assert unique_sorted([]) == []


def test_word_counts() -> None:
    text = "cola cola jameson cola"
    assert word_counts(text) == {"cola": 3, "jameson": 1}
    assert word_counts("") == {}
    assert word_counts("  a\tb\na  ") == {"a": 2, "b": 1}


def test_top_n() -> None:
    counts = {"cola": 3, "apple": 3, "jameson": 1, "water": 5}
    assert top_n(counts, 2) == [("water", 5), ("apple", 3)]
    assert top_n(counts, 10) == [
        ("water", 5),
        ("apple", 3),
        ("cola", 3),
        ("jameson", 1),
    ]
    assert top_n({}, 3) == []


def test_flatten() -> None:
    assert flatten([[1, 2], [], [3]]) == [1, 2, 3]
    assert flatten([]) == []


def test_even_squares() -> None:
    assert even_squares([1, 2, 3, 4]) == [4, 16]
    assert even_squares([1, 3]) == []


def test_total_by_year() -> None:
    rows = [
        ("jameson", 2007, 800.0),
        ("cola", 2007, 50.0),
        ("jameson", 2024, 2100.0),
        ("cola", 2024, 140.0),
    ]
    assert total_by_year(rows) == {2007: 850.0, 2024: 2240.0}
    assert total_by_year([]) == {}
