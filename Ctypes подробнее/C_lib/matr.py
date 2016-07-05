from ctypes import *
import time 

C = CDLL("./C_lib.so") #Подключение библиотеки на C

#N = int(input('Введите N - размерность матрицы: '))
N = 100

C_vect = c_int * N # тип - массив 
C_pointer = POINTER(C_vect) # тип - указатель на массив 
C_matr = C_pointer * N # тип - массив указателей на масивы

# Описываем возвращаемые типы для функций из файла на С
C.matr_max.restype = C_pointer

# Функция vect преобразоовывает список (list) в массив из N элементов
# типа c_int и возвращает указатель на него.
def vect(A): 
    res = C_vect()
    for i in range(len(A)):
        res[i] = c_int(A[i])
    return pointer(res)

# Функция matr преобразоовывает  двумерный список (list) в массив из N элементов
# типа c_pointer и возвращает указатель на него.
def matr(A):
    res = C_matr()
    for i in range(N):
        res[i] = vect(A[i])
    return pointer(res)

def get_matr(n):
    A = []
    print('Введодите матрицу построчно, элементы записывайте через пробел:')
    for i in range(n):
        A.append(list(map(int,input().split())))
    return(A)

A  = [[1,2,3],[4,5,6],[7,8,9]]
#A = get_matr(N)
A = []
for i in range(N):
    A.append(list())
    for j in range(N):
        A[i].append(j)
        

m = matr(A)

start = time.time()
for i in range(N):
    t = C.matr_max(m,c_int(N))
Ctime = time.time() - start

#for i in range(N):
#    print('Максимальный элемент из строки №',i+1,'=',t.contents[i])

ans = []
start = time.time()
for k in range(N):
    for i in range(N):
        max_A = A[i][0]
        for j in range(1,N):
            max_A = max(max_A,A[i][j])
        ans.append(max_A)
Pytime = time.time() - start        

#for i in range(N):
#    print('Максимальный элемент из строки №',i+1,'=',ans[i])

print(Ctime)
print(Pytime)
print(Pytime/Ctime)
