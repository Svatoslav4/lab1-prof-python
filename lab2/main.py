#варіатн 17

import math

def z(x, eps=1e-12):
    """Повертає значення виразу або None, якщо знаменник ~ 0 або невизначений."""
    denom = math.sin(3 * x) - x
    if abs(denom) < eps:
        return None
    return (6 * x + 4) / denom

start = 2.3
end = 7.8
step = 0.9

x = start
# захист проти нескінченного циклу через похибки плаваючої точки
max_iters = 1000
it = 0

print("  x\t\tz(x)")
print("-" * 30)
while x <= end + 1e-9 and it < max_iters:
    val = z(x)
    if val is None:
        print(f"{x:.6g}\t\tвираз не визначений (ділення на нуль або дуже малий знаменник)")
    else:
        print(f"{x:.6g}\t\t{val:.10g}")
    x += step
    it += 1
