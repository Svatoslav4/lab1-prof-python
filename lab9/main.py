import os

# ✅ Створення файлу з даними студентів
def create_file(filename):
    students = [
        ("Іваненко Іван", 89),
        ("Петров Петро", 75),
        ("Сидоренко Олег", 92),
        ("Коваль Анна", 85)
    ]
    with open(filename, "w", encoding="utf-8") as file:
        for name, grade in students:
            file.write(f"{name};{grade}\n")
    print(f"Файл '{filename}' створено ✅")


# ✅ Дозапис у файл
def append_student(filename, name, grade):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{name};{grade}\n")
    print("Студента додано ✅")


# ✅ Читання файлу
def read_file(filename):
    print("\n📌 Дані студентів:")
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())


# ✅ Пошук файлів у каталозі
def search_files(directory, filename_part):
    print("\n🔍 Пошук файлів у каталозі:")
    for file in os.listdir(directory):
        if filename_part in file:
            print("Знайдено:", file)


# ✅ Пошук студента у файлі
def find_student(filename, student_name):
    print(f"\n🔍 Пошук студента: {student_name}")
    with open(filename, "r", encoding="utf-8") as file:
        found = False
        for line in file:
            name, grade = line.strip().split(";")
            if student_name.lower() in name.lower():
                print(f"{name} — Середній бал: {grade}")
                found = True

        if not found:
            print("Студента не знайдено ❌")


# ✅ Сортування за середнім балом
def sort_by_grade(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = []
        for line in file:
            name, grade = line.strip().split(";")
            data.append((name, int(grade)))

    data.sort(key=lambda x: x[1], reverse=True)

    with open(filename, "w", encoding="utf-8") as file:
        for name, grade in data:
            file.write(f"{name};{grade}\n")

    print("\n📊 Дані відсортовано за середнім балом (спаданням) ✅")


# === ТЕСТ РОБОТИ ПРОГРАМИ ===
filename = "students.txt"

create_file(filename)
append_student(filename, "Мельник Олеся", 78)
read_file(filename)

sort_by_grade(filename)
read_file(filename)

search_files(".", "student")
find_student(filename, "Анна")
