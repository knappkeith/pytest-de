import datetime


def today_weekday() -> str:
    """Function to return the string of the weekday of today"""
    today = datetime.date.today()
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    return weekdays[today.weekday()]
