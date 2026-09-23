def fizzbuzz(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


def countdown(n: int) -> list[int]:
    list = []
    while n > 0:
        list.append(n)
        n -= 1
    return list


def sum_range(start: int, stop: int) -> int:
    sum = 0
    for n in range(start, stop):
        sum = sum + n
    return sum


def classify_status(code: int) -> str:
    ty = code // 100
    match ty:
        case 2:
            return "success"
        case 3:
            return "redirect"
        case 4:
            return "client_error"
        case 5:
            return "server_error"
        case _:
            return "other"


def first_even(xs: list[int]) -> int | None:
    for n in xs:
        if n % 2 == 0:
            return n
