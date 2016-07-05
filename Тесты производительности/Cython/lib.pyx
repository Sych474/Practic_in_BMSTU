INF = 10**6
N = 500
NAME = 'list'+str(N)+'.txt'
def get_lens(start):
	matr_file = open(NAME)	
	K = int(matr_file.readline())
	F = []
	for i in range(N):
		if i != start:
			F.append(INF)
		if i == start:
			F.append(0)
	matr = [[INF if i != j else 0 for i in range(N)] for j in range(N)]
	M = int(matr_file.readline())
	for k in range(M):
		i,j,val = map(int,matr_file.readline().split())
		matr[i][j] = val
	for k in range(N-1):
		for i in range(N):
			for j in range(N):
				if F[i] + matr[i][j] < F[j]:
					F[j] = F[i] + matr[i][j]
	matr_file.close()
	return (F)

