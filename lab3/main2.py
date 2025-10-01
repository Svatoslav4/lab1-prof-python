# Приклад списку
b = [3, -2, 5, -1, 4, -6, 2]

# Знаходимо індекс останнього додатного елемента
last_positive_index = -1
for i in range(len(b)):
    if b[i] > 0:
        last_positive_index = i

# Якщо додатні елементи є, обчислюємо суму до останнього включно
if last_positive_index != -1:
    total_sum = sum(b[:last_positive_index + 1])
    print("Сума до останнього додатного елемента включно:", total_sum)
else:
    print("У списку немає додатних елементів.")


