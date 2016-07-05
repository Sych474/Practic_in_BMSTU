from ctypes import *
import numpy as np
import time

A = []
C = CDLL("./C_lib2.0.so") #Подключение библиотеки на C

def Get_from_file_py(N):
    name = 'matr'+str(N)+'.txt'
    f = open(name)
    matr = []
    for i in range(N):
        matr.append(list(map(int,f.readline().rstrip().split())))
    return matr


def Get_matr_C(N): # Возвращает List из int  
    C_vect = c_int * N # тип - массив 
    C_matr = C_vect * N # тип - матрица
    matr = C_matr()
    C.prepair_matr(c_int(N),matr)
    D = np.array(matr,dtype = c_int)
    return D.tolist()

def Get_numpy_C_int(N): # Возвращает numpy.array из int32 
    C_vect = c_int * N # тип - массив 
    C_matr = C_vect * N # тип - матрица
    matr = C_matr()
    C.prepair_matr(c_int(N),matr)
    D = np.array(matr,dtype = int)
    return D

def Get_ctypes_int(N): # Возвращает матрицу из элементов типа C_int (тип из ctypes) 
    C_vect = c_int * N # тип - массив 
    C_matr = C_vect * N # тип - матрица
    matr = C_matr()
    C.prepair_matr(c_int(N),matr)
    return matr

def Get_matr_py_append(N): # Заполняет List при помощи append
    A = []
    for i in range(N):
        A.append(list())
        for j in range(N):
            A[i].append(j+i)
    return (A)

def Get_numpy_py(N): # Возвращает numpy.ndarray 
    D = np.ndarray(shape = (N,N),dtype = int)
    for i in range(N):
        for j in range(N):
            D[i][j] = (j+i)
    return D

def Get_numpy_py1(N):
    return np.array([[j+i for j in range(N)]for i in range(N)])

def Get_matr_py_generate(N): # Заполняет List генератором
    return [[j+i for j in range(N)]for i in range(N)]

N_val = [100,500,1000,1500,2000,2500,3000]
#N_val = [100,200]
print('Матрица заполняется по правилу: matr[i][j] = i + j')
print('Время заполениня матрицы N на N (приведено в миллисиекундах):')
print('     N        C->int     C->numpy    C->ctypes|       numpy       append    generator  ')
'''
for N in N_val:
    print('{:7d}'.format(N),end = ' ')
    start = time.time()
    Matr = Get_matr_C(N)
    print('{:12.2f}'.format((time.time()-start)*1000),end = ' ')

    start = time.time()
    Matr = Get_numpy_C_int(N)
    print('{:12.2f}'.format((time.time()-start)*1000),end = ' ')

    start = time.time()
    Matr = Get_ctypes_int(N)
    print('{:12.2f}'.format((time.time()-start)*1000),end = '|')

    start = time.time()
    Matr = Get_matr_py_append(N)
    print('{:12.2f}'.format((time.time()-start)*1000),end = ' ')

    start = time.time()
    Matr = Get_numpy_py(N)
    print('{:12.2f}'.format((time.time()-start)*1000),end = ' ')

    start = time.time()
    Matr = Get_matr_py_generate(N)
    print('{:12.2f}'.format((time.time()-start)*1000))

print('Слева от черты - способы с применением ctypes, справа - без применения этой библиотеки. ')
'''
def get_matr_max_C(N):
    C_vect = c_int * N # тип - массив 
    C_matr = C_vect * N # тип - матрица
    matr = C_matr()
    C.prepair_matr(c_int(N),matr)
    Number = C_vect()
    C.matr_max(c_int(N),matr,Number)
    return Number

def get_matr_max_Py(N):
    matr = [[j+i for j in range(N)]for i in range(N)]
    Max = [max(matr[i]) for i in range(N)]
    return Max

print()
print('Время нахождения максимумов по строкам (с учетом заполнения матрицы):')
print('     N     C->ctypes           py    ') #+'C->ctypes|       numpy       append    generator  ')    
for N in N_val:
    print('{:7d}'.format(N),end = ' ')
    start = time.time()
    Max = get_matr_max_C(N)
    print('{:12.2f}'.format((time.time()-start)*1000),end = ' ')

    start = time.time()
    Max = get_matr_max_Py(N)
    print('{:12.2f}'.format((time.time()-start)*1000),end = ' ')
    
    start = time.time()
    Matr = Get_from_file_py(N)
    print('{:12.2f}'.format((time.time()-start)*1000),end = '|')
    '''
    start = time.time()
    Matr = Get_matr_py_append(N)
    print('{:12.2f}'.format((time.time()-start)*1000),end = ' ')

    start = time.time()
    Matr = Get_numpy_py(N)
    print('{:12.2f}'.format((time.time()-start)*1000),end = ' ')

    start = time.time()
    Matr = Get_matr_py_generate(N)
    print('{:12.2f}'.format((time.time()-start)*1000))
'''
    print()
CONFIG = 'pc'

print ('\nКонфигурация:')
if CONFIG == 'net':
    print('Процессор: Intel Atom 1,33Ghz')
    print('RAM: 2 Гб')
elif CONFIG == 'pc':
    print('Процессор: Intel Core I5-4210U CPU 1,70Ghz')
    print('RAM: 4 Gb')


