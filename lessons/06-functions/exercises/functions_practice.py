SCALE = 10


def greet(name: str, greeting: str = "Hello") -> str:
    raise NotImplementedError


def join_words(*parts: str, sep: str = " ") -> str:
    raise NotImplementedError


def apply_twice(fn, x):
    raise NotImplementedError


def make_adder(n: int):
    raise NotImplementedError


def scaled(x: int, scale: int | None = None) -> int:
    raise NotImplementedError


def positive_only(xs: list[int]) -> list[int]:
    raise NotImplementedError
