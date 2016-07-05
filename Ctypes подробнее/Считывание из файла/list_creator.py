from random import*
INF = 10**6

def create_matr(N,probability):
    print(probability)
    matr = [[INF if i != j else 0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                if randint(1,100) < probability:
                    matr[i][j] = randint(1,10**4)
    return matr

def write_matr(name, N, matr):
    matr_file = open(name,'w')
    to_file = [str(N),'0']
    for i in range(N):
        for j in range(N):
            if matr[i][j] != INF and matr[i][j] != 0 :
                to_file[1] = str(int(to_file[1])+1)
                to_file.append(str(i)+' '+str(j)+' '+str(matr[i][j])) 
    for line in to_file:
        print(line, file = matr_file)
    matr_file.close()

def is_cicle(N,matr):
    cicle_found = False
    for start in range(N):
        F = [INF]*N
        F[start] = 0
        for k in range(N-1):
            for i in range(N):
                for j in range(N):
                    if F[i] + matr[i][j] < F[j]:
                        F[j] = F[i] + matr[i][j]  
        for i in range(N):
            for j in range(N):
                if F[i] + matr[i][j] < F[j]:
                    cicle_found = True 
    return cicle_found

N = int(input('Введите N: '))
P = float(input('Введите вероятность существвания ребра: '))
matr = create_matr(N,int(P*100//1))
write_matr('list'+str(N)+'.txt', N, matr)
print('Done!')
