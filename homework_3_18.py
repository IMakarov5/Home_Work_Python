# Задача 18: Требуется найти в массиве A[1..N] самый 
# близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#      1 2 3 4 5
#      6
#      -> 5

import random

while True:
    try:
        N = int( input("Введите количество элиментов в массиве: "))
        A = []

        for i in range(N):
            A.append(random.randint(0,10))

        print("Массив А: ",A)

        X = int (input('Введите числе X: '))

        M = A[0]
       

        for i in range(1,N):
           if A[i] == X or M < A[i] < X or X > A[i] > M :
                  M = A[i]
       
        print ("Данное число встречаеться: ", M)
        
        
        break
    except:
        print('Некорректный ввод. Попробуйте еще раз!')

