from list_utils import first_five_min, sum_list, max_element, min_element

def main():
    numbers = [12, 5, 7, 3, 19, 1, 9, 4, 8, 2]

    print("Список чисел:", numbers)
    print("Перші п'ять мінімальних елементів:", first_five_min(numbers))
    print("Сума елементів списку:", sum_list(numbers))
    print("Максимальний елемент списку:", max_element(numbers))
    print("Мінімальний елемент списку:", min_element(numbers))

if __name__ == "__main__":
    main()
