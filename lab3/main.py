import random

# Генеруємо матрицю випадкових чисел
rows, cols = 4, 5
a = [[random.randint(1, 50) for _ in range(cols)] for _ in range(rows)]

print("Початкова матриця:")
for row in a:
    print(row)

# Знаходимо індекс рядка з мінімальним елементом
min_val = a[0][0]
min_row = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] < min_val:
            min_val = a[i][j]
            min_row = i

# Міняємо місцями перший рядок і рядок з мінімальним елементом
a[0], a[min_row] = a[min_row], a[0]

print("\nМатриця після обміну рядків:")
for row in a:
    print(row)
