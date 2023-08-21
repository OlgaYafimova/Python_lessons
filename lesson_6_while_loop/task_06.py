"""Задание № 6
Простейший калькулятор c введёнными двумя числами вещественного типа.
Ввод с клавиатуры: операции + - * / и два числа.
Обработать ошибку: “Деление на ноль”
Ноль использовать в качестве завершения программы (сделать как отдельную
операцию)."""

while True:
    print("Введение нуля в качестве знака операции остановит работу")
    user_first_number = float(input("Введите первое число: "))
    user_choise_operation = input("Введите операцию (+ - * /): ")
    if user_choise_operation == '0':
        break
    user_second_number = float(input("Введите второе число: "))
    if user_choise_operation == '+':
        print(user_first_number + user_second_number)
    if user_choise_operation == '-':
        print(user_first_number - user_second_number)
    if user_choise_operation == '*':
        print(user_first_number * user_second_number)
    if user_choise_operation == '/':
        if user_second_number == 0:
            print("Делить на ноль нельзя")
        else:
            print(user_first_number / user_second_number)
