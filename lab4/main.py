# Введення речення
sentence = input("Введіть речення: ")

# Розбиваємо речення на слова
words = sentence.split()

# Шукаємо слово, що починається на 'к' або 'К'
found = False
for word in words:
    if word.lower().startswith("к"):
        print("Слово, що починається на 'к':", word)
        found = True
        break  # можна вивести лише перше знайдене слово

if not found:
    print("У реченні немає слів, що починаються на 'к'.")
