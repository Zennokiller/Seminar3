# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
n = int(input("Введите значение N:" ))
A = [i for i in range(1, n+1)]
X = int(input("Введите значение X:" ))
delta = X
item = -1
for i in range(0,n):
    if delta<(X-A[1]):
        delta = X-A[1]
        item = i #запонимаем индекс
print(A[item])