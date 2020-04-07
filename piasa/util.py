# piasa.util

CENT = 2 ** (1 / 1200)


def is_int(obj: object) -> bool:
    """Predicate, determines if argument may be converted to int."""
    try:
        int(obj)
        return True
    except ValueError:
        return False


def meter_to_feet(m: float) -> float:
    return 3.28084 * m


def feet_to_meter(f: float) -> float:
    return f / 3.28084

