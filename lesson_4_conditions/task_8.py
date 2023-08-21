"""Задание №8
Написать примитивный калькулятор. Пользователь должен ввести число, потом операцию (+-/*) и потом
ещё одно число, после этого пользователь получает ответ. Числа могут быть дробными"""

user_num1 = float(input("Введите 1-е число: "))
user_operation = input("Введите математическую операцию ('+' - сложение; '-' - вычитание, '*' - умножение, '/' - деление): ")
user_num2 = float(input("Введите 2-е число: "))


if user_operation == "+":
    print(user_num1 + user_num2)
elif user_operation == "-":
    print(user_num1 - user_num2)
elif user_operation == "*":
    print(user_num1 * user_num2)
elif user_operation == "/":
    if user_num2 == 0:
        print("Так делать нельзя!")
    else:
        print(user_num1 / user_num2)
else:
    print("Неправильно введён оператор")
