import lib

N = 100
start = (input('Введите начальную вершину: '))
F = lib.get_lens(int(start))
for i in range(N): #Вывод результата
	print(F[i])


	