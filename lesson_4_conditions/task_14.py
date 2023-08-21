"""Задача 14

Человек вводит день и месяц своего рождения,
выведите, кем он является по знаку зодиака"""

day = int(input("Введите день вашего рождения: "))
month = int(input("Введите номер месяца вашего рождения: "))
if 21 <= day <= 31 and month == 3 or 1 <= day <= 19 and month == 4:
    print("Вы Овен")
elif 21 <= day <= 31 and month == 4 or 1 <= day <= 20 and month == 5:
    print("Вы Телец")
elif 21 <= day <= 31 and month == 5 or 1 <= day <= 20 and month == 6:
    print("Вы Близнецы")
elif 21 <= day <= 30 and month == 6 or 1 <= day <= 22 and month == 7:
    print("Вы Рак")
elif 23 <= day <= 31 and month == 7 or 1 <= day <= 22 and month == 8:
    print("Вы Лев")
elif 23 <= day <= 31 and month == 8 or 1 <= day <= 22 and month == 9:
    print("Вы Дева")
elif 23 <= day <= 30 and month == 9 or 1 <= day <= 22 and month == 10:
    print("Вы Весы")
elif 23 <= day <= 31 and month == 10 or 1 <= day <= 21 and month == 11:
    print("Вы Скорпион")
elif 22 <= day <= 30 and month == 11 or 1 <= day <= 21 and month == 12:
    print("Вы Стрелец")
elif 22 <= day <= 31 and month == 12 or 1 <= day <= 19 and month == 1:
    print("Вы Козерог")
elif 20 <= day <= 31 and month == 1 or 1 <= day <= 18 and month == 2:
    print("Вы Водолей")
elif 19 <= day <= 29 and month == 2 or 1 <= day <= 20 and month == 3:
    print("Вы Рыбы")
else:
    print("Неправильна введена дата!")
