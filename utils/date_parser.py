from datetime import datetime, timedelta, timezone

def parse_date(date_str: str) -> datetime | None:
    """
    Parse a date string into a datetime object (always zeroed to midnight UTC).
    Supports 'today', 'tomorrow', 'yesterday', and 'YYYY-MM-DD' formats.
    """
    if not date_str:
        return None
    
    date_str = date_str.strip().lower()
    now = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    
    if date_str == "today":
        return now
    elif date_str == "tomorrow":
        return now + timedelta(days=1)
    elif date_str == "yesterday":
        return now - timedelta(days=1)
    else:
        try:
            # Try to parse standard YYYY-MM-DD
            parsed = datetime.strptime(date_str, "%Y-%m-%d")
            return parsed.replace(tzinfo=timezone.utc)
        except ValueError:
            return None
