# 1. Перемножить все нечётные значения в диапазоне от 1 до 100.
# 2. Записать в массив все числа в диапазоне от 1 до 500 кратные 5.
# 3. Вывести на экран все чётные значения в диапазоне от 1 до 497.
# 4. Дан массив чисел. Если число встречается более двух раз, то добавить
# его в новый массив.

# 1
count = 1
for i in range(1, 101):
    if i % 2 != 0:
        count *= i
print(count)

# 2
list_even = []
for i in range(1, 501):
    if i % 5 == 0:
        list_even.append(i)
print(list_even)

# 3
for i in range(1, 498):
    if i % 2 == 0:
        print(i)

# 4
mass = [1, 2, 3, 4, 5, 3, 4, 8, 6, 5, 1, 2, 3, 4, 7, 9]
mass_2 = []
for i in mass:
    if mass.count(i) > 2 and i not in mass_2:
        mass_2.append(i)
print(mass_2)
