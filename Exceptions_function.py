# Пункты задачи:

# 1. Создайте функцию personal_sum на основе условий задачи:


def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for num in numbers:
        try:
            result += float(num)  # Пробуем преобразовать к числу
        except (ValueError, TypeError):
            print(f"Некорректный тип данных для подсчёта суммы - {num}")
            incorrect_data += 1

    return result, incorrect_data

# 2. Создайте функцию calculate_average на основе условий задачи:

def calculate_average(numbers):
    try:
        # Проверяем, является ли переданный аргумент коллекцией
        if not isinstance(numbers, (list, tuple, set)):
            raise TypeError("В numbers записан некорректный тип данных")

        result_sum, incorrect_data = personal_sum(numbers)

        # Среднее арифметическое
        try:
            average = result_sum / (len(numbers) - incorrect_data)
            return average
        except ZeroDivisionError:
            return 0

    except TypeError as e:
        print(str(e))
        return None

# 3. Вызовите функцию calculate_average несколько раз, передав в неё данные разных вариаций:

# Примеры вызова функции
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается: => None
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Некорректные типы данных: => 2: 2.0
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция: => None
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Все данные корректные: => 26.5

print(f'Результат 5: {calculate_average([])}') # пустая коллекция: => 0