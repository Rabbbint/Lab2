def get_square(num_list):
    """ Функция принимает список чисел и возвращает список квадратов этих чисел """
    return [num ** 2 for num in num_list]

# Ввод списка чисел с клавиатуры
input_numbers = input("Введите список чисел через пробел: ").split()
numbers = [float(num) for num in input_numbers]

squared_numbers = get_square(numbers)
print("Квадраты введенных чисел:", squared_numbers)
