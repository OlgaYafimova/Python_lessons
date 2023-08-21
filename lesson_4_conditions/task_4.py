"""Задание №4
Вводятся три целых числа. Определить какое из
них наибольшее."""

us_num1 = int(input("Введите число: "))
us_num2 = int(input("Введите число: "))
us_num3 = int(input("Введите число: "))

if us_num2 < us_num1 > us_num3:
    print(f"{us_num1} больше всех")
elif us_num1 < us_num2 > us_num3:
    print(f"{us_num2} больше всех")
else:
    print(f"{us_num3} больше всех")
