INF = 10**6

def get_matr(name):
	matr_file = open(name)	
	N = int(matr_file.readline())
	matr = [[INF if i != j else 0 for i in range(N)] for j in range(N)]
	M = int(matr_file.readline())
	for k in range(M):
		i,j,val = map(int,matr_file.readline().split())
		matr[i][j] = val
	matr_file.close()
	return matr

def Ford_Bellman(matr,start):
	N = len(matr)
	F = [INF for i in range(N)]
	F[start] = 0
	for k in range(N-1):
		for i in range(N):
			for j in range(N):
				if F[i] + matr[i][j] < F[j]:
					F[j] = F[i] + matr[i][j]
	return (F)

N = 100
start = int(input('Введите начальную вершину: '))
matr = get_matr('list.txt')
F = Ford_Bellman(matr,1)
for i in range(N): #Вывод результата
	print(F[i])
