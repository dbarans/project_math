def add(a: int, b: int):
    return a + b


def sub(a: int, b: int):
    return a - b


def div(a: int, b: int):
    if b == 0:
        return print("dzielenie przez zero")
    else:

        return a / b


def mul(a: int, b: int):
    return a * b


def rownanie_kwadr(a: int, b: int, c: int):
    delta = b ** 2 - 4 * a * c
    x1 = (-b + delta ** (1 / 2)) / 2 * a
    x2 = (-b - delta ** (1 / 2)) / 2 * a
    if x1 == x2:
        return x1
    elif type(x1) == complex:
        return "brak rozwiązań"

    else:
        return x1, x2



