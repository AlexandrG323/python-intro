def should_run_cli(module_name: str) -> bool:
    if module_name == "__main__":
        return True
    return False


def describe_run_mode(imported: bool) -> str:
    if imported:
        return "library"
    return "script"
