import datetime


def convert_to_utc_time(date_str: str) -> datetime.datetime:
    """Returns the parsed date in UTC."""
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        # Format for dates with an explicit timezone offset
        date = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")

    if date.tzinfo:
        return date.astimezone(datetime.timezone.utc)

    return date
