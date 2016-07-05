#include <stdio.h>
#define N 10

struct vector
{
    int arr[N];
};

struct matr
{
    struct vector arr[N];
};

int max_in_row(struct vector mas)
{
    int i,max = mas.arr[0];
    for (i = 1; i < N; i++)
        if (mas.arr[i] > max) max = mas.arr[i];
    return max;
}

struct vector max_in_rows(struct matr M)
{
    int i,j;
    struct vector vect;
    for (i = 0; i < N; i++)
        vect.arr[i] = max_in_row(M.arr[i]);
    return vect;

}
