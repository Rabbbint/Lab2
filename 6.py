def words_starting_with_letter(word_list, letter):
    return [word for word in word_list if word.startswith(letter)]

# Ввод списка слов с клавиатуры
input_words = input("Введите список слов через пробел: ").split()
letter = input("Введите букву для фильтрации: ")

filtered_words = words_starting_with_letter(input_words, letter)
print(f"Слова, начинающиеся с буквы '{letter}': {filtered_words}")
