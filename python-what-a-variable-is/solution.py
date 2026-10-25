def compute_total(price: float, quantity: int) -> float:
    subtotal = price * quantity
    tax = (subtotal * 8) / 100
    subtotal += tax 
    return subtotal


def swap_two_variables(a, b):
    c = a
    a = b
    b = c
    return a,b
