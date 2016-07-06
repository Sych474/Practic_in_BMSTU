from ctypes import *

C = CDLL("./lib.so")

print('Работа со структурами')

print('Получение структуры из функции на С:')
#объявляем структуру, эквивалентную объявленной в библиотеке на C
class point(Structure):
	_fields_ = [("x",c_int),("y",c_int),("z",c_int)]

# Указываем возвращаемый тип функции 
C.get_point.restype = point 

p = point()

x = 1
y = 2
z = 3
print('x =',x)
print('y =',y)
print('z =',z)

#В функцию передаются x,y,z, функция возвращает структуру p
p = C.get_point(x,y,z)
print('Поля полученной структуры')
print('p.x =',p.x)
print('p.y =',p.y)
print('p.z =',p.z)
print('Тип полученной структуры:', type(p),'\n\n')

print('Передача структуры в функцию на C')
# Создаем новую структуру
p2 = point()
p2.x = 4
p2.y = 3
p2.z = 2

print('p2.x =',p2.x)
print('p2.y =',p2.y)
print('p2.z =',p2.z)

print('Результат вызова:',C.get_x(p2)) #Функция возвращает значение координаты x