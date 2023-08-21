"""Задание № 2
Перемножить все чётные значения в диапазоне от 0 до 125;
результат вывести на экран."""

counter = 1
result = 1
while counter < 126:
    if counter % 2 == 0:
        result *= counter
        print(result)
    counter += 1
print(counter)
