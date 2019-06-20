/*
 * 编写程序tail，将其输入中的最后n行打印出来。
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXLINE 1000

int getline(char line[], int maxline);

char linebuf[10000];

int main(int argc, char **argv)
{
    int len, line_num, i;
    int n = 10;
    char *lineptr[MAXLINE];
    char *p = linebuf;
    char line[MAXLINE];

    while (--argc > 0) 
    {
        if ((*(++argv))[0] == '-')
            if ((n = atoi(*argv + 1)) == 0)
                n = 10;
    }

    i = 0;
    while ((len = getline(line, MAXLINE)) > 0)
    {
        strcpy(p, line);
        lineptr[i++] = p;
        p += len + 1;
    }
    line_num = i;
    i = (n < line_num) ? (line_num - n) : 0;
    for (; i < line_num; ++i)
    {
        printf("%s", lineptr[i]);
    }

    return 0;
}

int getline(char s[], int lim)
{
    int c, i;

    for (i = 0; i < lim - 1 && (c = getchar()) != EOF && c != '\n'; ++i)
        s[i] = c;
    if (c == '\n')
    {
        s[i] = c;
        ++i;
    }
    s[i] = '\0';

    return i;
}
