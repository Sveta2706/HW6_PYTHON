# Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.


# a1 = int(input('Введите первый номер члена a1: '))
# d = int(input('Введите разность ар.пр. : '))
# k = int(input('Введите последний номер члена k: '))

# result = []

# for i in range(k):
#     result.append(a1+i*d)

# print('\nВсе члены прогрессии', ' '.join([str(x) for x in result]))

# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

mas=[random.randint(-50, 50) for i in range(random.randint(10,20))]

print(*mas)

maxi=int(input("MAX= "))

mini=int(input("MIN= "))

masi=[]

if maxi>=mini:

   for i in range(len(mas)):

      if maxi>=mas[i] and mini<=mas[i]:

          masi.append(i)

   print("Кол-во:",len(masi))
