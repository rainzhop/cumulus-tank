/*
 * 运用printd函数的设计思想编写一个递归版本的itoa函数，
 * 即通过递归调用把整数转换为字符串。
 */

#include <string.h>

void reverse(char s[]);

void itoa(int n, char s[])
{
    if (n == 0)
    {
        s[0] = '0';
        s[1] = '\0';
        return;
    }
    char t[100];
    int nn;
    int i = 0;
    int sign = 1;
    if (n < 0)
        sign = -1;

    s[0] = sign * (n % 10) + '0';
    s[1] = '\0';

    if ((nn = sign * (n / 10)) == 0)
        return;
    itoa(nn, t);
    reverse(t);
    strcat(s, t);
    i = strlen(s);

    if (sign == -1)
        s[i++] = '-';
    s[i] = '\0';
    reverse(s);

    return;
}

void reverse(char s[])
{
    int c, i, j;
    for (i = 0, j = strlen(s) - 1; i < j; ++i, --j)
    {
        c = s[i];
        s[i] = s[j];
        s[j] = c;
    }

    return;
}
