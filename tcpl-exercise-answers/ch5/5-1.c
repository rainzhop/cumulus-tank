/*
 * 在上面的例子中，如果符号+或-的后面紧跟的不是数字，
 * getint函数将把符号视为数字0的有效表达方式。
 * 修改该函数，将这种形式的+或-符号重新写回到输入流中。
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

int getint(int *pn)
{
    char t;
    int c, sign;

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
        *pn = 10 * *pn + (c - '0');
    *pn *= sign;
    if (c != EOF)
        ungetch(c);
    return c;
}
