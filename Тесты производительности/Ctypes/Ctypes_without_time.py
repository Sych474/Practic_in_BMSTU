from ctypes import *

N = 100
start = int(input('Введите начальную вершину: '))
C = CDLL("./Ctypes.so") #Подключение библиотеки на C
C_vect = c_int * N # тип - вектор
F = C_vect()
start = c_int(int(start))
C.Get_lens(N, start, F)
for i in range(N): # вывод результата
	print(F[i])
