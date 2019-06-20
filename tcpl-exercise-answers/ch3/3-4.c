/*
 * 在数的对二的补码表示中，我们编写的itoa函数不能处理最大的负数，
 * 即n等于-(2^字长 - 1)的情况。修改该函数，使它在任何机器上运行时都能打印出正确的值。
 */

#include <string.h>

void reverse(char s[]);

void itoa(int n, char s[])
{
    int i = 0;
    int sign = 1;
    if (n < 0)
        sign = -1;

    do
        s[i++] = sign * (n % 10) + '0';
    while ((n /= 10) != 0);
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
