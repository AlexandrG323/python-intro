SCALE = 10


def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


def join_words(*parts: str, sep: str = " ") -> str:
    return sep.join(parts)


def apply_twice(fn, x):
    return fn(fn(x))


def make_adder(n: int):
    def adder(x: int) -> int:
        return x + n

    return adder


def scaled(x: int, scale: int | None = None) -> int:
    if scale is None:
        return x * SCALE
    return x * scale


def positive_only(xs: list[int]) -> list[int]:
    return [x for x in xs if x > 0]
