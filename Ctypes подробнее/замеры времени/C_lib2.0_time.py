from ctypes import *
import numpy as np
import time

C = CDLL("./C_lib2.0.so") #Подключение библиотеки на C

N = int(input('Введите N - размерность матрицы: '))
A = []

#print('Введодите матрицу построчно, элементы записывайте через пробел:')
#for i in range(n):
#    A.append(list(map(int,input().split())))

start = time.time()

A = []
for i in range(N):
    A.append(list())
    for j in range(N):
        A[i].append(j+i)

print('Время заполнения для Py:', time.time() - start)

C_vect = c_int * N # тип - массив 
C_matr = C_vect * N # тип - матрица

start = time.time()

matr = C_matr()
C.prepair_matr(c_int(N),matr)

print('Время заполнения для С:', time.time() - start)

print('N:',N)

start = time.time()

max_val = C_vect()
C.matr_max(c_int(N),matr,max_val) #Вызов функции из C_lib2.0.so

print('Время работы функции в C:',time.time() - start)

#for i in range(N):
#    print('Максимальный элемент из строки №',i+1,'=',max_val[i])

start = time.time()

ans = [0]*N
for i in range(N):
    A_max = A[i][0]
    for j in range(N):
        if A_max < A[i][j]:
            A_max = A[i][j]
    ans[i] = A_max

print('Python:', time.time() - start)

start = time.time()

ans = [max(A[i]) for i in range(N)]

print('Python with max:', time.time() - start)
       
