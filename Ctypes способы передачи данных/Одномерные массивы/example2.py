from ctypes import *

C = CDLL("./lib.so")


print('Работа с массивом:')

N = 5

# объявляем тип "массив" и создаем переменну этого типа 
C_array = c_int * N
vect = C_array()

print('Массив до обработки:')

for i in range(N):
	vect[i] = i+10 # задаем начальные значения
	print('vect['+str(i)+'] =',vect[i])


C.get_array(N,vect) #Функция запишет в каждый элемент номер этого элемента

print('Результат:')

for i in range(N):
	print('vect['+str(i)+'] =',vect[i])

print('Тип массива vect: ',type(vect))
print('Тип элемента этого массива: ',type(vect[0]))