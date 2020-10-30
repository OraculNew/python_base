def to_float(x):
    result = 0
    try:
        result = float(x)
    except ValueError:
        pass
    return result


def to_int(x):
    result = 0
    try:
        result = int(x)
    except ValueError:
        pass
    return result
