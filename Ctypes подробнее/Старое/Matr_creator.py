from random import randint
def prerair_file(N):
    name = 'matr'+str(N)+'.txt'
    f = open(name,'w')
    for i in range(N):
        for j in range(N):
            f.write(str(randint(-2**16,2**16))+' ')
        f.write('\n')
    f.close()
    print(N,'done')

N_val = [100,500,1000,1500,2000,2500,3000]
for N in N_val:
    prerair_file(N)
