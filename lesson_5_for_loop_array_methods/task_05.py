"""Задание № 5
Дан массив чисел. Найти их сумму и произведение."""

list1 = [1, 2, 3, 4, 5]
sum_of_list = sum(list1)
print(f"Сумма списка: {sum_of_list}")

count = 1
for i in list1:
    count *= i
print(f"Произведение списка: {count}")
