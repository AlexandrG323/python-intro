import pytest

from pick_language import pick_language


def test_esp32_firmware_is_cpp() -> None:
    assert pick_language("Flash firmware to ESP32") == "cpp"


def test_arduino_gpio_is_cpp() -> None:
    assert pick_language("Read GPIO on Arduino") == "cpp"


def test_microcontroller_is_cpp() -> None:
    assert pick_language("Bare-metal microcontroller loop") == "cpp"


def test_nestjs_api_is_typescript() -> None:
    assert pick_language("Build a NestJS REST API") == "typescript"


def test_react_frontend_is_typescript() -> None:
    assert pick_language("React frontend for the cart page") == "typescript"


def test_csv_analysis_is_python() -> None:
    assert pick_language("Analyze whisky prices CSV") == "python"


def test_llm_script_is_python() -> None:
    assert pick_language("Write a script that calls an LLM") == "python"


def test_notebook_dataset_is_python() -> None:
    assert pick_language("Explore a dataset in a notebook") == "python"


def test_pandas_is_python() -> None:
    assert pick_language("Aggregate rows with pandas") == "python"


def test_hardware_beats_script_keywords() -> None:
    assert pick_language("ESP32 script that toggles GPIO") == "cpp"


def test_unknown_job_raises() -> None:
    with pytest.raises(ValueError, match="unknown job"):
        pick_language("rewrite the compiler backend")
