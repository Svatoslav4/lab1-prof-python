class Vehicle:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def display_info(self):
        print(f"Марка: {self.__brand}, Модель: {self.__model}, Рік: {self.__year}")


class Car(Vehicle):
    def __init__(self, brand, model, year, seats):
        super().__init__(brand, model, year)
        self.__seats = seats

    def display_info(self):
        super().display_info()
        print(f"Кількість місць: {self.__seats}\n")


class Truck(Vehicle):
    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)
        self.__load_capacity = load_capacity

    def display_info(self):
        super().display_info()
        print(f"Вантажопідйомність: {self.__load_capacity} кг\n")


# ✅ Робота з колекцією об'єктів
vehicles = [
    Car("Toyota", "Corolla", 2020, 5),
    Car("BMW", "X5", 2022, 5),
    Truck("Volvo", "FH16", 2019, 20000),
    Truck("MAN", "TGX", 2021, 25000)
]


# ✅ Пошук за маркою
def find_by_brand(brand):
    print(f"Результати пошуку для марки: {brand}")
    found = False
    for v in vehicles:
        if v.get_brand().lower() == brand.lower():
            v.display_info()
            found = True
    if not found:
        print("Нічого не знайдено!\n")

# ✅ Тест виведення
print("📌 Усі транспортні засоби: \n")
for v in vehicles:
    v.display_info()

print("\n🔍 Пошук за конкретною ознакою:\n")
find_by_brand("BMW")
find_by_brand("Audi")
