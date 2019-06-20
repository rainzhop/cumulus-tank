#include <stdio.h>
#include "calc.h"

#define MAXVAL    100

int sp = 0;
double val[MAXVAL];

void push(double f)
{
    if (sp < MAXVAL)
        val[sp++] = f;
    else
        printf("error: stack full, can't push %g\n", f);
}

double pop(void)
{
    if (sp > 0)
        return val[--sp];
    else
    {
        //printf("error: stack empty\n");
        return 0.0;
    }
}

void print_top(void)
{
    printf("stack top: %.8f\n", val[sp - 1]);
    return;
}

double copy_top(void)
{
    return val[sp - 1];
}

void swap_top(void)
{
    double tmp = val[sp - 1];
    val[sp - 1] = val[sp - 2];
    val[sp - 2] = tmp;
    return;
}

void clear(void)
{
    while (sp > 0)
        val[sp--] = 0;
    val[sp] = 0;
    return;
}
