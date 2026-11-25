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


def call_with_retry(fn, attempts=4, base=0.5, sleep=time.sleep):
    for attempt in range(attempts):
        try:
            return fn()
        except APIError as error:
            if not is_retryable(error) or attempt == attempts - 1:
                raise
            sleep(backoff_delay(attempt, base))
