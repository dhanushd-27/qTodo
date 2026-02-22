from datetime import datetime

def format_date(date_val):
    """
    Format a datetime object or ISO string to a human-readable string.
    """
    if not date_val:
        return ""
    if isinstance(date_val, str):
        try:
            # Handle standard ISO formats, including trailing 'Z' for UTC
            date_val = datetime.fromisoformat(date_val.replace('Z', '+00:00'))
        except ValueError:
            return date_val
    if hasattr(date_val, 'strftime'):
        return date_val.strftime("%d %m %Y")
    return str(date_val)
