from control_flow import classify_status, countdown, first_even, fizzbuzz, sum_range


def test_fizzbuzz() -> None:
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"


def test_countdown() -> None:
    assert countdown(3) == [3, 2, 1]
    assert countdown(1) == [1]
    assert countdown(0) == []
    assert countdown(-2) == []


def test_sum_range() -> None:
    assert sum_range(1, 5) == 10
    assert sum_range(5, 5) == 0
    assert sum_range(-2, 2) == -2


def test_classify_status() -> None:
    assert classify_status(200) == "success"
    assert classify_status(201) == "success"
    assert classify_status(301) == "redirect"
    assert classify_status(404) == "client_error"
    assert classify_status(500) == "server_error"
    assert classify_status(99) == "other"
    assert classify_status(600) == "other"


def test_first_even() -> None:
    assert first_even([1, 3, 4, 6]) == 4
    assert first_even([2]) == 2
    assert first_even([1, 3, 5]) is None
    assert first_even([]) is None
