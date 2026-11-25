def is_retryable(error):
    status = getattr(error, "status", None)
    return status in (429, 529)


def backoff_delay(attempt, base=0.5):
    return base * 2 ** attempt
