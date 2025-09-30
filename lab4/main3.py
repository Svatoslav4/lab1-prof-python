
text = input("Введіть текст (латинські літери): ")


vowels = set("aeiouy")


found_vowels = sorted(set(text) & vowels)


if found_vowels:
    print("Голосні, що зустрічаються в тексті:", " ".join(found_vowels))
else:
    print("У тексті немає голосних.")
