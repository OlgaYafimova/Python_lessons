"""Задание №5
Напишите игру камень, ножницы, бумага.
В качестве хода компьютера используйте
числа от 1 до 3 соответствующе.
Решить через модуль random"""

import random

dict_val = {
    1: "камень",
    2: "ножницы",
    3: "бумага"
}

count = 0
win_user = 0
win_comp = 0
while count < 11:
    user = int(input("Введите камень (1), ножницы (2) или бумага (3): "))
    computer = random.randint(1, 3)
    if user == 1 and computer == 1:
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              f"Ваш выбор: {dict_val[user]}\n"
              f"Компьютер выбрал: {dict_val[computer]}\n"
              f"НИЧЬЯ!!!")
        count += 1
    elif user == 2 and computer == 2:
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              f"Ваш выбор: {dict_val[user]}\n"
              f"Компьютер выбрал: {dict_val[computer]}\n"
              f"НИЧЬЯ!!!")
        count += 1
    elif user == 3 and computer == 3:
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              f"Ваш выбор: {dict_val[user]}\n"
              f"Компьютер выбрал: {dict_val[computer]}\n"
              f"НИЧЬЯ!!!")
        count += 1
    elif user == 1 and computer == 2:
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              f"Ваш выбор: {dict_val[user]}\n"
              f"Компьютер выбрал: {dict_val[computer]}\n"
              f"КАМЕНЬ ЗАТУПИЛ НОЖНИЦЫ!!!\n"
              f"ВЫ ВЫИГРАЛИ!!!")
        count += 1
        win_user += 1
    elif user == 1 and computer == 3:
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              f"Ваш выбор: {dict_val[user]}\n"
              f"Компьютер выбрал: {dict_val[computer]}\n"
              f"БУМАГА ЗАВОРАЧИВАЕТ КАМЕНЬ!!!\n"
              f"ВЫ ПРОИГРАЛИ!!!")
        count += 1
        win_comp += 1
    elif user == 2 and computer == 1:
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              f"Ваш выбор: {dict_val[user]}\n"
              f"Компьютер выбрал: {dict_val[computer]}\n"
              f"КАМЕНЬ ЗАТУПИЛ НОЖНИЦЫ!!!\n"
              f"ВЫ ПРОИГРАЛИ!!!")
        count += 1
        win_comp += 1
    elif user == 2 and computer == 3:
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              f"Ваш выбор: {dict_val[user]}\n"
              f"Компьютер выбрал: {dict_val[computer]}\n"
              f"НОЖНИЦЫ РЕЖУТ БУМАГУ!!!\n"
              f"ВЫ ВЫИГРАЛИ!!!")
        win_user += 1
        count += 1
    elif user == 3 and computer == 1:
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              f"Ваш выбор: {dict_val[user]}\n"
              f"Компьютер выбрал: {dict_val[computer]}\n"
              f"БУМАГА ЗАВОРАЧИВАЕТ КАМЕНЬ!!!!!!\n"
              f"ВЫ ВЫИГРАЛИ!!!")
        win_user += 1
        count += 1
    elif user == 3 and computer == 2:
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              f"Ваш выбор: {dict_val[user]}\n"
              f"Компьютер выбрал: {dict_val[computer]}\n"
              f"НОЖНИЦЫ РЕЖУТ БУМАГУ!!!\n"
              f"ВЫ ПРОИГРАЛИ!!!")
        count += 1
        win_comp += 1
    else:
        print("неправильно введён номер")
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
      f"Всего игр сыграно: {count}\n"
      f"Победы компьютера: {win_comp}\n"
      f"Ваши победы: {win_user}")
