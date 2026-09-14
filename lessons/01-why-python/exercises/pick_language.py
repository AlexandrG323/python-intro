def pick_language(job: str) -> str:
    """Return 'cpp', 'typescript', or 'python' for a short job description."""
    jobwork: dict[str, list[str]] = {
        "cpp": ["arduino", "esp32", "firmware", "microcontroller", "gpio"],
        "typescript": ["react", "nestjs", "frontend"],
        "python": ["csv", "script", "pandas", "llm", "dataset", "notebook"],
    }

    for language, jobs in jobwork.items():
        if any(word.lower() in job.lower() for word in jobs):
            return language

    raise ValueError("unknown job")
