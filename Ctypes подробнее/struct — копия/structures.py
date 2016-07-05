from ctypes import *

C_struct = CDLL("./struct.so")
N = 10
class vector (Structure):
    _fields_ = [("arr", (c_int)*N)]

class matr (Structure):
    _fields_ = [("arr", vector*N)]

C_struct.max_in_rows.restype = vector

t = matr()
print('Матрица, передаваемая в функцию на C')
for i in range(N):
    for j in range(N):
        t.arr[i].arr[j] = i*j
        print(t.arr[i].arr[j],end = ' ')
    print()
v = C_struct.max_in_rows(t)

print('Массив максимумов по строкам:')
for i in range(N):
    print(v.arr[i],end = ' ')
print()

