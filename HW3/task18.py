# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих строках записаны
#  N целых чисел Ai. Последняя строка содержит число X

# n = 5
# 1 2 3 4 5
# x = 6
# -> 5


import random
array = []
n = int(input("Введите величину случайно-заполняемого  массива : "))
j =  0
count = 0
for i in range(0, n):
    array.append(random.randrange(1, 11, 1))           
print(f'Ваш массив : \n {array}')
k = int(input("Введите число которое вы хотите тут найти (от 1 до 10): "))
while j < n:
    if array[j] == k:
        if j == 0:
            print(f'ближайшее число : {array[array.index(array[j+1])]}')
            count += 1
        else:
            print(f'ближайшее число : {array[array.index(array[j-1])]}')
            count += 1
    j += 1
if count == 0:
    print("Число в масиве не встретилось, попробуй в другой раз. ")
print("  КОНЕЦ  ")