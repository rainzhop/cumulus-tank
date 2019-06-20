/*
 * 模仿getint的实现方法，编写一个读取浮点数的函数getfloat。
 */

#include <stdio.h>
#include <ctype.h>

#define BUFSIZE 100

char buf[BUFSIZE];
int bufp = 0;

int getch(void)
{
    return (bufp > 0) ? buf[--bufp] : getchar();
}

void ungetch(int c)
{
    if (bufp >= BUFSIZE)
        printf("ungetch: too many characters\n");
    else
        buf[bufp++] = c;
}

int getfloat(double *pn)
{
    char t;
    int c, sign;
    double power;

    while (isspace(c = getch()))
        ;
    if (!isdigit(c) && c != EOF && c != '+' && c != '-') 
    {
        //ungetch(c);
        return 0;
    }
    t = c;
    sign = (c == '-') ? -1 : 1;
    if (c == '+' || c == '-')
        c = getch();
    if (!isdigit(c))
    {
        ungetch(t);
        return 0;
    }
    for (*pn = 0; isdigit(c); c = getch())
        *pn = 10.0 * *pn + (c - '0');
    if (c == '.')
        c = getch();
    for (power = 1.0; isdigit(c); c = getch())
    {
        *pn = 10.0 * *pn + (c - '0');
        power /= 10.0;
    }
    *pn = *pn * sign * power;
    if (c != EOF)
        ungetch(c);
    return c;
}
