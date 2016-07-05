#include <stdio.h>

#define MAXN 1000

int res[MAXN];

int max_in_row( int vect[],int n)
{
    int i,result = vect[0];
    for (i = 1;i < n;i++)
        if (vect[i]>result)
            result = vect[i];
    return result;
}

int *matr_max(int *vect[],int n)
{
    int i,k = 0;
    for (i = 0;i < n;i++)
    {
        *(res+i) = max_in_row((vect[i]),n);
        k+=max_in_row((vect[i]),n);
    }
    return  res;
}
