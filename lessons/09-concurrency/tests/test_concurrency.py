from threading import Lock

import pytest

from concurrency import cpu_bound_sum, gil_held_for, increment_safely, pick_tool


def test_cpu_bound_sum() -> None:
    assert cpu_bound_sum(5) == 10
    assert cpu_bound_sum(0) == 0
    assert cpu_bound_sum(-3) == 0
    assert cpu_bound_sum(1) == 0


def test_increment_safely() -> None:
    counter = {"value": 0}
    lock = Lock()
    increment_safely(counter, 100, lock)
    assert counter["value"] == 100


def test_pick_tool() -> None:
    assert pick_tool("ESP32 firmware updater") == "sync"
    assert pick_tool("Download JSON from HTTP API wait") == "asyncio"
    assert pick_tool("Compress pixels on all CPU cores") == "multiprocessing"
    assert pick_tool("Read blocking files from disk") == "threading"
    assert pick_tool("Print hello") == "sync"


def test_hardware_beats_cpu_keyword() -> None:
    assert pick_tool("firmware cpu burn-in") == "sync"


def test_gil_held_for() -> None:
    assert gil_held_for("pure-python-loop") is True
    assert gil_held_for("time.sleep") is False
    assert gil_held_for("file-read") is False
    with pytest.raises(ValueError):
        gil_held_for("gpu")
