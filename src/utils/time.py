import datetime


def convert_to_utc_time(date):
    """Returns the parsed date in UTC."""
    try:
        date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        # Format for dates with an explicit timezone offset
        date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")

    if date.tzinfo:
        date = date.astimezone(datetime.timezone.utc)

    return date
