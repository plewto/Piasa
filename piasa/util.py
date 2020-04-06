# piasa.util

def is_int(obj: object) -> bool:
    try:
        int(obj)
        return True
    except ValueError:
        return False

