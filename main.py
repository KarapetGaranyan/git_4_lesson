def is_even(number):
    """Проверяет, является ли число четным"""
    return number % 2 == 0

def get_max(a, b, c):
    """Находит максимальное из трех чисел"""
    return max(a, b, c)

def celsius_to_fahrenheit(celsius):
    """Конвертирует температуру из Цельсия в Фаренгейт"""
    return (celsius * 9/5) + 32


# Примеры использования
print(is_even(4))  # Выведет True
print(is_even(7))  # Выведет False

print(get_max(10, 5, 8))  # Выведет 10

print(celsius_to_fahrenheit(0))   # Выведет 32.0
print(celsius_to_fahrenheit(100)) # Выведет 212.0

# добавили левую функцию из ветки test
def greeting(name):
    """Создает персонализированное приветствие"""
    return f"Привет, {name}!"


