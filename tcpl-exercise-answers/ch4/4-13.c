/*
 * 编写一个递归版本的reverse(s)函数，以将字符串s倒置。
 */

#include <string.h>

void reverse(char s[])
{
    char c;
    int sl = strlen(s);
    if (sl == 1)
        return;

    c = s[sl - 1];
    s[sl - 1] = '\0';
    reverse(s);

    s[sl] = '\0';
    while (--sl > 0)
        s[sl] = s[sl - 1];
    s[0] = c;

    return;
}
