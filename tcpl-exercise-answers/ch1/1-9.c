/*
 * 编写一个将输入复制到输出的程序，并将其中连续的多个空格用一个空格代替。
 */

#include <stdio.h>

int main()
{
    char c;
    char prev = EOF;


    while ((c = getchar()) != EOF)
    {
        if (c == ' ' && c == prev)
            continue;
        putchar(c);
        prev = c;
    }

    return 0;
}
