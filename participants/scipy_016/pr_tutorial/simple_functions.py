def fibonacci(n_terms: int) -> list:
    values = [0, 1]
    while len(values) < n_terms:
        values.append(values[-2] + values[-1])
    return values


def factorial(value: int):
    if value == 0:
        return 1

    return value * factorial(value - 1)
