from ctypes import *
import time

INF = 10**6
start = 1
name = 'list75.txt'
start_time = time.time()
matr_file = open(name)	
N = int(matr_file.readline())

class vector (Structure):
    _fields_ = [("arr", (c_int)*N)]

class matr (Structure):
    _fields_ = [("arr", vector*N)]

def print_matr(matr):
	for i in range(N):
		for j in range(N):
			print(matr.arr[i].arr[j],end = ' ')
		print()

def print_vector(vect):
	for i in range(N):
		print(vect.arr[i])	

matrix = matr()
for i in range(N):
	for j in range(N):
		matrix.arr[i].arr[j] = INF
M = int(matr_file.readline())
for k in range(M):
	i,j,val = map(int,matr_file.readline().split())
	matrix.arr[i].arr[j] = val
matr_file.close()
#print('here 1')
C_struct = CDLL("./structures.so")
C_struct.Ford_Bellman.restype = vector
F = vector()
#print('here 2')
F = C_struct.Ford_Bellman(matrix,start)
#print('here 3')
print((time.time()-start_time)*1000)

