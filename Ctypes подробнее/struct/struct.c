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

struct point
{
    int x;
    int y;
};

struct vector vector_init(void)
{
     int i,j;
     struct vector v;
     for (i = 0; i < N; i++)
        v.arr[i] = i;
     return v;
}

struct matr matr_init(void)
{
     int i,j;
     struct matr m;
     for (i = 0; i < N; i++)
        m.arr[i] = vector_init();
     return m;
}


struct point point_init(void)
{
     int i;
     struct point p;
     p.x = 1;
     p.y = 2;
     return p;
}
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
