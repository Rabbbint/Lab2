def count_vowels_and_consonants(sentence):
    vowels = "аеёиоуыэюя"
    consonants = "бвгджзйклмнпрстфхцчшщ"

    vowel_count = 0
    consonant_count = 0

    for char in sentence:
        if char.isalpha():
            if char.lower() in vowels:
                vowel_count += 1
            elif char.lower() in consonants:
                consonant_count += 1

    return vowel_count, consonant_count


# Ввод предложения с клавиатуры
input_sentence = input("Введите предложение на русском языке: ")

vowel_count, consonant_count = count_vowels_and_consonants(input_sentence)

print("Количество гласных букв:", vowel_count)
print("Количество согласных букв:", consonant_count)
