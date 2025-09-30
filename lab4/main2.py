
text = input("Введіть текст (цифри та літери латиницею): ")


vowels = set("aeiouyAEIOUY")


vowel_count = 0
consonant_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1


print("Кількість голосних:", vowel_count)
print("Кількість приголосних:", consonant_count)

if vowel_count > consonant_count:
    print("У тексті більше голосних.")
elif consonant_count > vowel_count:
    print("У тексті більше приголосних.")
else:
    print("Голосних і приголосних однакова кількість.")
