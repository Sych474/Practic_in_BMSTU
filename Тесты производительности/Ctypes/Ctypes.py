from ctypes import *
import time

N = 100

M = 20
time_val = 0
start = 1
print('Время приведено в милисекундах (0.001 с)')

print('Количество запусков =',M)
for i in range(M):
	
	start_time = time.time()
	C = CDLL("./Ctypes.so") #Подключение библиотеки на C
	C_vect = c_int * N # тип - вектор
	F = C_vect()
	start = c_int(1)
	C.Get_lens(N, start, F)
	time_val +=(time.time()-start_time)
	print((time.time()-start_time)*1000)

print('Среднее время работы Ctypes:', '{:14.2f}'.format(time_val/M*1000),'мс.')