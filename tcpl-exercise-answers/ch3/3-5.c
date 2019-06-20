/*
 * 编写函数itob(n, s, b)，将整数n转换为以b为底的数，
 * 并将转换结果以字符的形式保存到字符串s中。
 * 例如，itob(n, s, 16)把整数n格式化成十六进制整数保存在s中。
 */

#include <string.h>

void reverse(char s[]);

void itob(int n, char s[], unsigned int b)
{
    int i = 0;
    int d;
    int sign = 1;
    if (n < 0)
        sign = -1;

    do
    {
        d = sign * (n % b);
        if (d > 9)
            s[i++] = d - 10 + 'A';
        else
            s[i++] = sign * (n % b) + '0';
    }
    while ((n /= b) != 0);

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
