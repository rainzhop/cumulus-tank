/*
 * 编写一个程序，根据自身被调用时存放在argv[0]中的名字，
 * 实现将大写字母转换为小写字母或小写字母转换为大写字母的功能。
 */

#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, char **argv)
{
    char name[100] = {0};
    char i, *p;
    int c;
    int toupper_flag = 0;

    i = 0;
    while (argv[0][i++] != '\0')
    {
        if (argv[0][i] == '/')
            p = argv[0] + i + 1;
    }
    strncpy(name, p, 5);
    if (strcmp(name, "upper") == 0)
        toupper_flag = 1;
    else if (strcmp(name, "lower") == 0)
        toupper_flag = 0;
    else
        return -1;

    while ((c = getchar()) != EOF)
    {
        if (toupper_flag == 1)
            c = toupper(c);
        else
            c = tolower(c);
        putchar(c);
    }

    return 0;
}