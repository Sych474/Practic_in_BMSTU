from ctypes import *
import numpy as np
import time

INF = 10**6

def get_matr_py(N): # Возвращает List N на N из int
	name = 'list' + str(N) + '.txt'
	matr_file = open(name)	
	M = int(matr_file.readline())
	matr = [[INF if i != j else 0 for i in range(N)] for j in range(N)]
	M = int(matr_file.readline())
	for k in range(M):
		i,j,val = map(int,matr_file.readline().split())
		matr[i][j] = val
	matr_file.close()
	return matr

def get_matr_Ctypes(N): # Возвращает C_matr
	C = CDLL("./C_lib.so")
	C_vect = c_int * N # тип - массив 
	C_matr = C_vect * N # тип - матрица
	matr = C_matr()
	C.read_matr(c_int(N),matr)
	return matr 

def get_matr_Ctypes_int(N): # Возвращает List N на N из int
	C = CDLL("./C_lib.so")
	C_vect = c_int * N # тип - массив 
	C_matr = C_vect * N # тип - матрица
	matr = C_matr()
	C.read_matr(c_int(N),matr)
	D = np.array(matr,dtype = c_int)
	return D.tolist()

def get_matr_Ctypes_numpy(N): # Возвращает numpy.array из int32 
	C = CDLL("./C_lib.so")
	C_vect = c_int * N # тип - массив 
	C_matr = C_vect * N # тип - матрица
	matr = C_matr()
	C.read_matr(c_int(N),matr)
	D = np.array(matr,dtype = int)
	return D



def get_time_py(N,M): # Возвращает время считывания в List (мс.) 
	time_val = 0
	for i in range(M):
		start_time = time.time()
		matr = get_matr_py(N)
		time_val +=(time.time()-start_time)
	return time_val/M*1000


def get_time_Ctypes(N,M): # Возвращает время считывания в C_matr (мс.) 
	time_val = 0
	for i in range(M):
		start_time = time.time()
		matr = get_matr_Ctypes(N)
		time_val +=(time.time()-start_time)
	return time_val/M*1000

def get_time_Ctypes_int(N,M): # Возвращает время считывания в List с помошью Ctypes (мс.) 
	time_val = 0
	for i in range(M):
		start_time = time.time()
		matr = get_matr_Ctypes_int(N)
		time_val +=(time.time()-start_time)
	return time_val/M*1000

def get_time_Ctypes_numpy(N,M):# Возвращает время считывания в numpy.array(мс.) 
	time_val = 0
	for i in range(M):
		start_time = time.time()
		matr = get_matr_Ctypes_numpy(N)
		time_val +=(time.time()-start_time)
	return time_val/M*1000


N_val = [10,50,100,200,300,400,500]
M = 10
print('Количество запусков =',M)
print('Время приведено в милисекундах (0.001 с)')
print('{:>4}|{:>20}|{:>20}|{:>20}|{:>20}'.format('N','Python->List','Ctypes->C_matr','Ctypes->List','Ctypes->numpy.array'))
for N in N_val:
	print('{:4d}|{:20.2f}|{:20.2f}|{:20.2f}|{:20.2f}'.format(N, get_time_py(N,M), get_time_Ctypes(N,M), get_time_Ctypes_int(N,M),get_time_Ctypes_numpy(N,M)))




CONFIG = 'pc'

print ('\nКонфигурация:')
if CONFIG == 'net':
    print('Процессор: Intel Atom 1,33Ghz')
    print('RAM: 2 Гб')
elif CONFIG == 'pc':
    print('Процессор: Intel Core I5-4210U CPU 1,70Ghz')
    print('RAM: 4 Gb')


