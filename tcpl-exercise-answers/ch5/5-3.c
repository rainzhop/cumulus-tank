/*
 * 用指针方式实现第2章中的函数strcat。
 * 函数strcat(s, t)将t指向的字符串复制到s指向的字符串的尾部。
 */

void strcat(char *s, char *t)
{
    while (*(++s) != '\0')
        ;
    while (*t != '\0')
        *(s++) = *(t++);
    *s = '\0';

    return;
}
