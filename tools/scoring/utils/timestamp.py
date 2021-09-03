from datetime import datetime, timezone


def timestamp() -> datetime:
    """Provides a reference for "now".

    Returns:
        A UTC datetime for the time of execution
    """
    return datetime.now(timezone.utc)
