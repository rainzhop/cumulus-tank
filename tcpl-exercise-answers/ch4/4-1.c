/*
 * 编写函数strrindex(s, t)，它返回字符串t在s中最右边出现的位置。
 * 如果s中不包含t，则返回-1。
 */

#include <string.h>

int strrindex(char s[], char t[])
{
    int i, j, k;
    int sl, tl;
    sl = strlen(s);
    tl = strlen(t);

    for (i = sl - 1; i >= tl - 1; --i)
    {
        k = i;
        j = tl - 1;
        while (j >= 0)
            if (s[k--] != t[j--])
                break;
        if (j < 0)
            return ++k;
    }

    return -1;
}
