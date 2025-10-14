def find_five_min_elements(numbers):
    """
    Функція знаходить перші п’ять мінімальних елементів у списку.
    Якщо елементів менше ніж 5 — повертає всі.
    """
    if not numbers:
        print("Список порожній.")
        return []

    # Сортуємо список за зростанням і беремо перші 5 елементів
    min_elements = sorted(numbers)[:5]

    print("Перші п’ять мінімальних елементів:", min_elements)
    return min_elements


# Приклад використання
numbers = [12, 3, 5, 7, 19, 2, 8, 1, 6, 4]
find_five_min_elements(numbers)
