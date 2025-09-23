#варіант 17

import math

def y(x):
    try:
        numerator = math.exp(-3 * x) + math.log(x - 1) ** 3
        denominator = math.log(abs(x + 1)) + math.tan(x ** 2 - 1)
        return numerator / denominator
    except (ValueError, ZeroDivisionError):
        return None  # якщо вираз не визначений

# приклад обчислення
for x in [2, 3, -0.5, 1.5]:
    print(f"x = {x}, y = {y(x)}")
