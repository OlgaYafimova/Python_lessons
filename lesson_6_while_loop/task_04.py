"""Задание № 4
Пользователь вводит два числа c клавиатуры, необходимо
вывести на экран все отрицательные числа, лежащие между
ними. Например пользователь ввёл -5 и 3, на экране вывелось
-4, -3, -2, -1"""

first_user_number = int(input("Введите первое число: "))
second_user_number = int(input("Введите второе число: "))

while first_user_number < second_user_number:
    first_user_number += 1
    if first_user_number == 0:
        break
    print(first_user_number)
