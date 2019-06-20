/*
 * 编写函数strend(s, t)。
 * 如果字符串t出现在字符串s的尾部，该函数返回1；否则返回0。
 */

int strend(char *s, char *t)
{
    int i, j;
    i = 0;
    j = 0;
    while (*(++s) != '\0')
        ++i;
    while (*(++t) != '\0')
        ++j;
    if (j > i)
        return 0;

    while (j-- >= 0)
        if (*(--s) != *(--t))
            return 0;

    return 1;
}
