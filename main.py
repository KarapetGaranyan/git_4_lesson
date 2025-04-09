def is_even(number):
    """Проверяет, является ли число четным"""
    return number % 2 == 0

def get_max(a, b, c):
    """Находит максимальное из трех чисел"""
    return max(a, b, c)

def celsius_to_fahrenheit(celsius):
    """Конвертирует температуру из Цельсия в Фаренгейт"""
    return (celsius * 9/5) + 32