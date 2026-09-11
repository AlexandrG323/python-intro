from app import run
from greeter import greet
from run_mode import describe_run_mode, should_run_cli


def test_greet_format() -> None:
    assert greet("Sasa") == "Hello, Sasa!"


def test_run_delegates_to_greeter() -> None:
    assert run("Lyceum") == "Hello, Lyceum!"


def test_cli_guard() -> None:
    assert should_run_cli("__main__") is True
    assert should_run_cli("greeter") is False
    assert should_run_cli("app") is False


def test_run_mode_labels() -> None:
    assert describe_run_mode(True) == "library"
    assert describe_run_mode(False) == "script"
