"""Задание №2
Пользователь вводит порядковый номер
пальца руки, надо вывести его название"""

user_number = int(input("Введите порядковый номер пальца: "))


def which_finger(num):
    if num == 1:
        print(f"{num} - большой палец")
    elif num == 2:
        print(f"{num} - указательный палец")
    elif num == 3:
        print(f"{num} - средний палец")
    elif num == 4:
        print(f"{num} - безымянный палец")
    elif num == 5:
        print(f"{num} - мизинец")
    else:
        print(f"{num} - нет такого пальца, вы чо, опухли? ☺")


which_finger(user_number)
