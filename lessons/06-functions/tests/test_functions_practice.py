from functions_practice import (
    SCALE,
    apply_twice,
    greet,
    join_words,
    make_adder,
    positive_only,
    scaled,
)


def test_greet() -> None:
    assert greet("Sasa") == "Hello, Sasa!"
    assert greet("Sasa", greeting="Привет") == "Привет, Sasa!"


def test_join_words() -> None:
    assert join_words("a", "b", "c") == "a b c"
    assert join_words("a", "b", sep="-") == "a-b"
    assert join_words() == ""


def test_apply_twice() -> None:
    assert apply_twice(lambda x: x + 1, 10) == 12
    assert apply_twice(str.upper, "ok") == "OK"


def test_make_adder() -> None:
    add5 = make_adder(5)
    add0 = make_adder(0)
    assert add5(3) == 8
    assert add0(3) == 3
    assert add5(0) == 5


def test_scaled_uses_module_constant() -> None:
    assert SCALE == 10
    assert scaled(3) == 30
    assert scaled(3, scale=2) == 6


def test_positive_only_does_not_mutate() -> None:
    xs = [-1, 0, 2, 5]
    assert positive_only(xs) == [2, 5]
    assert xs == [-1, 0, 2, 5]
    assert positive_only([]) == []
