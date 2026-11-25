def is_retryable(error):
    status = getattr(error, "status", None)
    return status in (429, 529)
