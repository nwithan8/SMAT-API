from datetime import datetime


def string_to_datetime(string: str, format: str = "%Y-%m-%dT%H:%M:%S.%f") -> datetime:
    return datetime.strptime(string, format)

def datetime_to_string(datetime_object: datetime, format: str = "%Y-%m-%dT%H:%M:%S.%f") -> str:
    return datetime_object.strftime(format)


def validate_dict(items: dict):
    for k, v in items.items():
        if v:
            accepted = accepted_values(key=k)
            if accepted:
                validate(key=k, value=v, accepted=accepted)


def accepted_values(key):
    if key == "site":
        return ["reddit", "twitter", "8kun", "4chan", "gab", "parler", "thedonald", "poal", "telegram"]
    elif key == 'interval':
        return ['hour', 'day', 'week', 'month']
    else:
        return []


def validate(key, value, accepted):
    if value not in accepted:
        raise Exception(f"Valid {key} options: {', '.join(accepted)}")
