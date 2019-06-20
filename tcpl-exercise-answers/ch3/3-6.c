/*
 * 修改itoa函数，使得该函数可以接收三个参数。其中，第三个参数为最小字段宽度。
 * 为了保证转换后所得的结果至少具有第三个参数制定的最小宽度，
 * 在必要时应在所得结果的左边补充一定的空格。
 */

#include <string.h>

void reverse(char s[]);

void itoa(int n, char s[], unsigned int w)
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
    while (i < w)
        s[i++] = ' ';

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
