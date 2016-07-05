#include <stdio.h>

#define INF 1000000
#define N 75


struct vector
{
    int arr[N];
};

struct matr
{
    struct vector arr[N];
};


struct vector Ford_Bellman(struct matr matrix, int srart)
{
	int i,j,k;
	struct vector F;
	for (i = 0; i < N; i++)
		F.arr[i] = INF;
    F.arr[srart] = 0;

    for (k = 0; k < N-1; k++)
        for (i = 0; i < N; i++)
            for (j = 0; j < N; j++)
                if (F.arr[i] + matrix.arr[i].arr[j] < F.arr[j])
					F.arr[j] = F.arr[i] + matrix.arr[i].arr[j];
	return F;
}
