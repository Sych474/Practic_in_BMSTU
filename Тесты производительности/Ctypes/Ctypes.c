#include <stdio.h>
#include <stdlib.h>

#define LEN 50
#define INF 1000000

void read_matr(const int N, const char name[LEN], int matr[N][N])
{
    int k, count, i, j, val;
    FILE *matr_file = fopen(name, "r");
    for (i = 0; i < N; i++)
        for (j = 0; j < N; j++)
            if (i == j)
                matr[i][j] = 0;
            else
                matr[i][j] = INF;
    fscanf(matr_file,"%d%d", &k,&count);
    for (k = 0; k < count; k++)
    {
    	fscanf(matr_file,"%d%d%d", &i, &j, &val);
    	matr[i][j] = val;
    }
    fclose(matr_file);
}

void Ford_Bellman(const int N,int matr[N][N], int F[],const int start)
{
    int i,j,k;
    for (i = 0; i < N; i++)
    {
        if (i != start)
            F[i] = INF;
        else
            F[start] = 0;
    }
    for (k = 0; k < N-1; k++)
        for (i = 0; i < N; i++)
            for (j = 0; j < N; j++)
                if (F[i] + matr[i][j] < F[j])
					F[j] = F[i] + matr[i][j];
}

void Get_lens(const int N, const int start, int F[])
{
    int matr[N][N];
    char name[LEN] = "list.txt";
    read_matr(N,name,matr);
    Ford_Bellman(N,matr,F,start);
}
