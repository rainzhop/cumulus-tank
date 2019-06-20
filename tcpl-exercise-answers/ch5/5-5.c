/*
 * 实现库函数strncpy、strncat和strncmp，它们最多对参数字符串中的前n个字符进行操作。
 * 例如，函数strncpy(s, t, n)将t中最多前n个字符复制到s中。
 */

char *strncpy(char *s, char *t, unsigned int n)
{
    while (n-- != 0)
        if (*t != '\0')
            *(s++) = *(t++);
        else
            *(s++) = '\0';

    return s;
}

char *strncat(char *s, char *t, unsigned int n)
{
    while (*(++s) != '\0')
        ;
    while (*t != '\0' && n-- != 0)
        *(s++) = *(t++);
    *s = '\0';

    return s;
}

int strncmp(char *s, char *t, unsigned int n)
{
    while (*s != '\0' && *t != '\0' && n-- != 0)
    {
        if (*s < *t)
            return -1;
        else if (*s > *t)
            return 1;
        ++s;
        ++t;
    }

    return 0;
}
