def unique_elements(input_list):
    return list(set(input_list))

# Ввод списка чисел с клавиатуры
input_numbers = input("Введите список чисел через пробел: ")
numbers = list(map(int, input_numbers.split()))

unique_numbers = unique_elements(numbers)
print("Уникальные элементы:", unique_numbers)1