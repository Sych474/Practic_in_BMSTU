#include <stdio.h>

void prepair_matr(const int N, int matr[][N])
{
    int i,j;
    for (i = 0; i < N; i++)
        for (j = 0; j < N; j++)
            matr[i][j] = i+j;
}

int max_in_row( int vect[], int n)
{
    int i, result = vect[0];
    for (i = 1; i < n; i++)
        if (vect[i] > result)
            result = vect[i];
    return result;
}

void matr_max(const int N, int matr[][N], int rep[])
{
    int i;
    for (i = 0; i < N; i++)
        rep[i] = max_in_row((matr[i]), N);
}
