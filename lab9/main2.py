# Ім'я вхідного та вихідного файлу
input_file = "input.txt"
output_file = "output.txt"

try:
    with open(input_file, "r", encoding="utf-8") as inp, \
         open(output_file, "w", encoding="utf-8") as out:

        for line in inp:
            if len(line.strip()) > 30:
                out.write(line)

    print("✅ Рядки успішно переписані у файл:", output_file)

except FileNotFoundError:
    print("❌ Помилка: Файл не знайдено! Перевірте назву input.txt")
