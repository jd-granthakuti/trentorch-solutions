def is_truthy(value) -> bool:
    print(type(value))
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
    """
    Return the first value in `values` that is truthy. If no
    value in the list is truthy, return None.
    Do not use Python's built-in `any()`, implement the scan
    explicitly using is_truthy-style checks.
    """
    pass
    for i in range(len(values)):
        if values[i]:
            return values[i]

    return None
