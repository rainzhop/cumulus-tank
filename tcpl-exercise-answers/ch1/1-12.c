/*
 * 编写一个程序，以每行一个单词的形式打印其输入。
 */

#include <stdio.h>

int main()
{
    char c, prev;
    prev = EOF;
    
    while ((c = getchar()) != EOF)
    {
        if (c == '\n' || c == ' ' || c == '\t')
            c = '\n';
        if (prev != '\n')
            putchar(c);
        prev = c;
    }

    return 0;
}
