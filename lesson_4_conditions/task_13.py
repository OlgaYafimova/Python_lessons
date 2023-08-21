"""Задача 13
Если переменная а равна 0 или 2, то прибавить ей 7, иначе поделить ее на 10.
Вывести новое значения переменной на экран"""

import random

rand_int = random.randint(0, 3)
print(rand_int)
if rand_int == 0 or rand_int == 2:
    rand_int += 7
    print(rand_int)
else:
    print(rand_int / 10)
