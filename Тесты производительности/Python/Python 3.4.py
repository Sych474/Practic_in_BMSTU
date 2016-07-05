import time
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

M = 1
time_val = 0
start = 1
print('Время приведено в милисекундах (0.001 с)')
print('Количество запусков =',M)
for i in range(M):
	
	start_time = time.time()
	matr = get_matr('list100.txt')
	F = Ford_Bellman(matr,1)
	time_val +=(time.time()-start_time)
	print((time.time()-start_time)*1000)

print('Среднее время работы Python:', '{:14.2f}'.format(time_val/M*1000),'мс.')
