from datetime import datetime


def string_to_datetime(
    string: str, date_format: str = "%Y-%m-%dT%H:%M:%S.%f"
) -> datetime:
    return datetime.strptime(string, date_format)


def datetime_to_string(
    datetime_object: datetime, date_format: str = "%Y-%m-%dT%H:%M:%S.%f"
) -> str:
    return datetime_object.strftime(date_format)


def validate_dict(items: dict):
    for k, v in items.items():
        if v:
            accepted = accepted_values(key=k)
            if accepted:
                validate(key=k, value=v, accepted=accepted)


def accepted_values(key):
    if key == "interval":
        return ["hour", "day", "week", "month"]
    else:
        return []


def validate(key, value, accepted):
    if value not in accepted:
        raise Exception(f"Valid {key} options: {', '.join(accepted)}")
