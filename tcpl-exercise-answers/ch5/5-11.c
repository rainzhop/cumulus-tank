/*
 * 修改程序detab，使其接受一组作为参数的制表符停止位。
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXLINE 1000

int getline(char line[], int maxline);
int detab(char s[], int len, unsigned int ts);

int main(int argc, char **argv)
{
    int len, i;
    unsigned int ts = 8;
    char line[MAXLINE];

    while ((len = getline(line, MAXLINE)) > 0)
    {
        if (argc == 0)
        {
            detab(line, len, ts);
            printf("%s", line);
        }
        
        for (i = 1; i < argc; ++i)
        {
            char tmp[MAXLINE];
            strcpy(tmp, line);
            ts = atoi(argv[i]);
            if (ts < 0)
                continue;
            detab(tmp, len, ts);
            printf("%s", tmp);
        }
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

int detab(char s[], int len, unsigned int ts)
{
    char tmp[MAXLINE] = { 0 };
    int i, j, space_num;

    for (i = 0; i < len; ++i)
        tmp[i] = s[i];

    space_num = 0;
    j = 0;
    for (i = 0; i < len; ++i)
    {
        if (tmp[i] == '\t')
        {
            space_num = j % ts;
            do
                s[j++] = ' ';
            while (++space_num < ts);
        }
        else
        {
            s[j++] = tmp[i];
        }
    }
    s[j] = '\0';

    return j;
}
