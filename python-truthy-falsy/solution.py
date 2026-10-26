def is_truthy(value) -> bool:
    if value is None:
        return False
    elif type(value) == int or type(value) == float:
        if value == 0 :
            return False
    elif type(value) is bool:
        if not value:
            return False
    elif len(value) == 0:
        return False
    return True


def first_truthy(values: list):
    for i in range(len(values)):
        if values[i]:
            return values[i]

    return None
