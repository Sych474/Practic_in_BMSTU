#include <stdio.h>
#include <stdlib.h>

#define LEN 20
#define INF 1000000

void read_matr(const int N, int matr[N][N])
{
    int k, count, i, j, val;
    char num[LEN];
    char name[LEN] = "list";
    itoa(N,num,10);
    i = 0;
    j = 4;
    while (num[i] != '\0')
        name[j++] = num[i++];
    name[j++] = '.';
    name[j++] = 't';
    name[j++] = 'x';
    name[j++] = 't';
    name[j++] = '\0';
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
