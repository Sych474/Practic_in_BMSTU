#include <stdio.h>

void get_array(const int N,int vect[N])
{
    int i;
    for (i = 0; i < N; i++)
        vect[i] = i;
}