"""Задание №5
Необходимо, чтоб программа выводила на экран вот такую
последовательность(не использовать готовый массив):
7 14 21 28 35 42 49 56 63 70 77 84 91 98
Добавить в массив и найти его длину."""

counter = 1
list_seven = []
while counter < 15:
    seven = 7
    multiplied = seven * counter
    print(multiplied, end=' ')
    list_seven.append(multiplied)
    counter += 1
print(f"\nДлина списка: {len(list_seven)}")
