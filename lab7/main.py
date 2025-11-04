from typing import Dict, List

class Worker:
    workers_list: List['Worker'] = []

    def __init__(self, full_name: str, info: Dict[str, any]):
        self.full_name = full_name
        self.department = info.get("department")
        self.position = info.get("position")
        self.birth_year = info.get("birth_year")
        self.experience = info.get("experience")
        Worker.workers_list.append(self)

    @classmethod
    def find_by_name(cls, name: str) -> List['Worker']:
        return [worker for worker in cls.workers_list if worker.full_name.lower() == name.lower()]

    @classmethod
    def find_by_department(cls, department: str) -> List['Worker']:
        return [worker for worker in cls.workers_list if worker.department.lower() == department.lower()]

    @classmethod
    def find_by_age(cls, age: int, current_year: int) -> List['Worker']:
        return [worker for worker in cls.workers_list if current_year - worker.birth_year == age]

    @classmethod
    def add_worker(cls, full_name: str, info: Dict[str, any]) -> 'Worker':
        return cls(full_name, info)

    @classmethod
    def remove_worker(cls, full_name: str) -> bool:
        found_workers = cls.find_by_name(full_name)
        if not found_workers:
            return False
        for worker in found_workers:
            cls.workers_list.remove(worker)
        return True

    def __str__(self):
        return (f"Прізвище та ім'я: {self.full_name}, Відділ: {self.department}, "
                f"Посада: {self.position}, Рік народження: {self.birth_year}, "
                f"Стаж: {self.experience} років")


if __name__ == "__main__":
    Worker.add_worker("Іваненко Іван", {"department": "Бухгалтерія", "position": "Бухгалтер", "birth_year": 1990, "experience": 5})
    Worker.add_worker("Петренко Петро", {"department": "IT", "position": "Програміст", "birth_year": 1995, "experience": 3})
    Worker.add_worker("Сидоренко Олена", {"department": "IT", "position": "Тестувальник", "birth_year": 1992, "experience": 4})

    print("Всі працівники:")
    for worker in Worker.workers_list:
        print(worker)

    print("\nПошук за ім'ям 'Петренко Петро':")
    for w in Worker.find_by_name("Петренко Петро"):
        print(w)

    print("\nПошук за відділом 'IT':")
    for w in Worker.find_by_department("IT"):
        print(w)

    current_year = 2025
    print("\nПошук за віком 30 років:")
    for w in Worker.find_by_age(30, current_year):
        print(w)

    print("\nВидалення працівника 'Іваненко Іван':")
    if Worker.remove_worker("Іваненко Іван"):
        print("Працівника видалено.")
    else:
        print("Працівника не знайдено.")

    print("\nВсі працівники після видалення:")
    for worker in Worker.workers_list:
        print(worker)
