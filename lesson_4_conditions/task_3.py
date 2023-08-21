"""Задание №3
Пользователь вводит номер месяца (от 1 до 12).
Вывести название сезона года на экран
(зима, весна, лето, осень)"""

user_number = int(input("Введите порядковый номер месяца: "))


def which_time_of_year(num):
    if num == 1 or num == 2 or num == 12:
        print("winter")
    elif num == 3 or num == 4 or num == 5:
        print("spring")
    elif num == 6 or num == 7 or num == 8:
        print("summer")
    elif num == 9 or num == 10 or num == 11:
        print("fall")
    else:
        print("there is no such a month, are you crazy? ☺")


which_time_of_year(user_number)
