from ctypes import *

C = CDLL("./lib.so")


print('Работа с целыми числами')
a = 1
b = 2

print('a =',a)
print('b =',b)

c = C.get_int(a,b) # Функция складывает два числа

print('Тип переменной, возвращенной функцией: ',type(c))
print('Значение переменной c: ',c)

print('\n\nРабота с действительными числами:')

a = 1.2
b = 2.2

print('a =',a)
print('b =',b)

# преобразуем типы в совместимые с C
a = c_float(1.2)
b = c_float(2.3)


C.get_float.restype = c_float # Указываем возвращаемый тип
c = C.get_float(a,b) # Функция складывает два числа

print('Тип переменной, возвращенной функцией: ',type(c))
print('Значение переменной с: ',c)