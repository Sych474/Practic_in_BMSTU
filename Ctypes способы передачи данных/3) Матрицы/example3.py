from ctypes import *

C = CDLL("./lib.so")

print('Работа с матрицей:')
N = 5

# Объявляем типы "массив" и "матрица" и создаем переменные этих типов 
C_array = c_int * N
C_matr = C_array *N
matr = C_matr()
vect = C_array()

print('Матрица до обработки:')
for i in range(N):
	for j in range(N):
		matr[i][j] = i+j+10
		print(matr[i][j],end = ' ')
	print()

C.get_matr(N,matr,vect) 
#Функция запишет в каждый элемент произведение строки на столбец, 
#а также в переданный массив vect, будут записаны суммы по строкам

print('Массив vect:')
for i in range(N):
	print('vect['+str(i)+'] =',vect[i])

print('Матрица после вызова функции:')
for i in range(N):
	for j in range(N):
		print(matr[i][j],end = ' ')
	print()

print('Тип матрицы: ',type(matr))
print('Тип элемента матрицы: ',type(matr[0][0]))

