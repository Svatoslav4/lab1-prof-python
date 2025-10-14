import math


# -------------------------------
# Функція, яку аналізуємо
# -------------------------------
def f(x):
    return math.sqrt(x) / (1 - x ** 2)


# -------------------------------
# Розклад sqrt(x) у ряд Тейлора біля x0 = 1
# sqrt(x) ≈ 1 + 1/2*(x-1) - 1/8*(x-1)^2 + 1/16*(x-1)^3 - ...
# -------------------------------
def sqrt_taylor(x, eps):
    term = 1  # перший член
    s = term
    n = 1
    dx = x - 1
    while True:
        # формула для коефіцієнтів розкладу sqrt(1+dx)
        term *= (0.5 - (n - 1)) * dx / n
        s_new = s + term
        if abs(s_new - s) <= eps:
            return s_new, n
        s = s_new
        n += 1


# -------------------------------
# Розклад 1/(1 - x^2) у ряд Тейлора: 1 + x^2 + x^4 + x^6 + ...
# -------------------------------
def one_over_one_minus_x2_taylor(x, eps):
    term = 1
    s = term
    n = 1
    while True:
        term *= x ** 2
        s_new = s + term
        if abs(s_new - s) <= eps:
            return s_new, n
        s = s_new
        n += 1


# -------------------------------
# Основна програма
# -------------------------------
def main():
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    eps = float(input("Введіть точність ε: "))
    m = int(input("Введіть кількість точок m (≥10): "))

    step = (b - a) / (m - 1)
    print(f"{'xᵢ':>8} | {'f(xᵢ) точне':>15} | {'fₙабл(xᵢ)':>15} | {'|Δ|':>10} | {'Ітерацій':>10}")
    print("-" * 70)

    for i in range(m):
        x = a + i * step
        try:
            # Точне значення
            f_exact = f(x)
            # Наближене через Тейлор
            sqrt_approx, n1 = sqrt_taylor(x, eps)
            denom_approx, n2 = one_over_one_minus_x2_taylor(x, eps)
            f_approx = sqrt_approx / denom_approx
            diff = abs(f_exact - f_approx)
            iterations = n1 + n2
            print(f"{x:8.4f} | {f_exact:15.8f} | {f_approx:15.8f} | {diff:10.2e} | {iterations:10}")
        except (ValueError, ZeroDivisionError):
            print(f"{x:8.4f} | {'—':>15} | {'—':>15} | {'—':>10} | {'—':>10}")


if __name__ == "__main__":
    main()
