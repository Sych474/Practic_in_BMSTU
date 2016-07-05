#include <stdio.h>

struct point
{
    int x;
    int y;
    int z;
};

struct point get_point(int x,int y,int z)
{
    struct point p;
    p.x = x;
    p.y = y;
    p.z = z;
    return (p);
}

int get_x(struct point p)
{
	return (p.x);
}