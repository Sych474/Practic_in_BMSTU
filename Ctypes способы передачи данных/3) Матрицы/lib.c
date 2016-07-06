#include <stdio.h>

void get_matr(const int N, int matr[][N],int ans[N])
{
    int i,j;
    for (i = 0; i < N; i++)
        for (j = 0; j < N; j++)
            ans[i] = matr[i][j];
    for (i = 0; i < N; i++)
        for (j = 0; j < N; j++)
            matr[i][j] = i*j;      
}


