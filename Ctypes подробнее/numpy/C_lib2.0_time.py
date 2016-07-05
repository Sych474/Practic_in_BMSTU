from ctypes import *
import numpy as np
import time

A = []
C = CDLL("./C_lib2.0.so") #Подключение библиотеки на C

N = int(input('Введите N - размерность матрицы: '))
C_vect = c_int * N # тип - массив 
C_matr = C_vect * N # тип - матрица


# Если начальные данные считываются из файла, или матрица задается по определенным правилам,
# то возможно ее заполнение на С и предача в Python 
start = time.time()
G_start = time.time()
matr = C_matr()
C.prepair_matr(c_int(N),matr)
print('Время заполнения матрицы на С:', '{:7.2f}'.format((time.time()-start)*1000))

#
start = time.time()
D = np.array(matr,dtype = c_int)
print('Время преобразования матрицы из матрицы для С вматрицу numpy:',
      '{:7.2f}'.format((time.time()-start)*1000))

start = time.time()
A = D.tolist()
print('Время преобразования из numpy к стандартной матрице int','{:7.2f}'.format((time.time()-start)*1000))
print('Общее время заполнения с использованием С и numpy','{:7.2f}'.format((time.time()-G_start)*1000))
start = time.time()

A = []
for i in range(N):
    A.append(list())
    for j in range(N):
        A[i].append(j+i)

print('Время заполнения для Py:', '{:7.2f}'.format((time.time()-start)*1000))
start = time.time()
max_val = C_vect()
C.matr_max(c_int(N),matr,max_val) #Вызов функции из C_lib2.0.so
print('Время работы функции в C:','{:7.2f}'.format((time.time()-start)*1000))


start = time.time()
def vect(A): 
    res = C_vect()
    for i in range(len(A)):
        res[i] = A[i]
    return res

# Функция matr преобразоовывает  двумерный список (list) в матрицу N на N элементов типа С_int
def matr(A):
    res = C_matr()
    for i in range(N):
        res[i] = vect(A[i])
    return res

v = matr(A)
print('Преобразование в массив С_int (для работы с функциями из библиотеки на С)'
      ,'{:7.2f}'.format((time.time()-start)*1000))
