import pytest

from names_and_copies import is_none, is_same_object, mutate_last, shallow_copy, swap


def test_is_same_object() -> None:
    xs = [1, 2]
    assert is_same_object(xs, xs) is True
    assert is_same_object(xs, [1, 2]) is False


def test_is_none() -> None:
    assert is_none(None) is True
    assert is_none(0) is False
    assert is_none("") is False
    assert is_none(False) is False


def test_shallow_copy_is_new_list() -> None:
    inner = [1]
    xs = [inner, 2]
    copied = shallow_copy(xs)
    assert copied == xs
    assert copied is not xs
    copied.append(3)
    assert xs == [[1], 2]
    assert copied[0] is inner


def test_mutate_last() -> None:
    xs = ["a", "b", "c"]
    mutate_last(xs, "z")
    assert xs == ["a", "b", "z"]


def test_mutate_last_empty_raises() -> None:
    with pytest.raises(IndexError):
        mutate_last([], "x")


def test_swap_returns_pair() -> None:
    assert swap(1, 2) == (2, 1)
    assert swap("left", "right") == ("right", "left")
