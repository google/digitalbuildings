from datetime import datetime, timezone

def timestamp() -> datetime:
    return datetime.now(timezone.utc)
