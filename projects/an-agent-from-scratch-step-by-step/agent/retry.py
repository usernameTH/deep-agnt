def is_retryable(error):
    status = getattr(error, "status", None)
    return status in (429, 529)


def backoff_delay(attempt, base=0.5):
    return base * 2 ** attempt


def retry_after(headers):
    if headers is None:
        return None
    key = headers.get('Retry-After')
    try:
        return int(key)
    except:
        return None
