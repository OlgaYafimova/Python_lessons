"""Задание № 7
Массив из 7 цифр. Если чётных цифр в нем больше, чем нечётных, то найти сумму всех его цифр,
если нечётных больше, то найти произведение 1, 3 и 6 элементов"""

l1 = [32, 64, 88, 11, 22, 66, 66]

list_even = []
list_odd = []
for i in l1:
    if i % 2 == 0:
        list_even.append(i)
    else:
        list_odd.append(i)
while True:
    if len(list_even) > len(list_odd):
        print(sum(l1))
    else:
        print(l1[0] * l1[2] * l1[5])
    break
