"""Задача 12
Дана строка из 3-цифр.  Найдите сумму этих цифр.
То есть сложите как числа первый символ строки, второй и третий."""

user_str = input("Введите числа: ")

count = 0
for i in user_str:
    count += int(i)
print(count)