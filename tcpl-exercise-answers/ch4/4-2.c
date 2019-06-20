/*
 * 对atof函数进行扩充，使它可以处理形如
 * 123.45e-6
 * 的科学表示法，其中，浮点数后面可能会紧跟一个e或E以及一个整数（可能有正负号）。
 */

#include <ctype.h>

double atof(char s[])
{
    double val, power;
    int i, j, sign, exp;

    for (i = 0; isspace(s[i]); ++i)
        ;
    sign = (s[i] == '-') ? -1 : 1;
    if (s[i] == '+' || s[i] == '-')
        ++i;
    for (val = 0.0; isdigit(s[i]); ++i)
        val = 10.0 * val + (s[i] - '0');
    if (s[i] == '.')
        ++i;
    for (power = 1.0; isdigit(s[i]); ++i)
    {
        val = 10.0 * val + (s[i] - '0');
        power /= 10.0;
    }
    val = sign * val;
    if (s[i] == 'e' || 'E')
        ++i;
    sign = (s[i] == '-') ? -1 : 1;
    if (s[i] == '+' || s[i] == '-')
        ++i;
    for (exp = 0; isdigit(s[i]); ++i)
        exp = 10 * exp + (s[i] - '0');
    for (j = 0; j < exp; ++j)
    {
        if (sign < 0)
            power /= 10.0;
        else
            power *= 10.0;
    }
    val = val * power;
    return val;
}
