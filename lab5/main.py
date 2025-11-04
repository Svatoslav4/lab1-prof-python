def find_five_min_elements(numbers):

    if not numbers:
        print("Список порожній.")
        return []


    min_elements = sorted(numbers)[:5]

    print("Перші п’ять мінімальних елементів:", min_elements)
    return min_elements



numbers = [12, 3, 5, 7, 19, 2, 8, 1, 6, 4]
find_five_min_elements(numbers)
