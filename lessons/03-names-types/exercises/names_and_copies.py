def is_same_object(a: object, b: object) -> bool:
    return a is b


def is_none(value: object) -> bool:
    return value is None


def shallow_copy(xs: list) -> list:
    return xs.copy()


def mutate_last(xs: list, value: object) -> None:
    xs[-1] = value


def swap(a: object, b: object) -> tuple:
    return b, a
