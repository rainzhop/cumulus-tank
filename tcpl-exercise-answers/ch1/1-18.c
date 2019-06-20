/*
 * 编写一个程序，删除每个输入行末尾的空格及制表符，
 * 并删除完全是空格的行。
 */

#include <stdio.h>

#define MAXLINE 1000

int getline(char line[], int maxline);
void copy(char to[], char from[]);
int del_space(char line[], int len);

int main()
{
    int len;
    int max;
    char line[MAXLINE];

    max = 0;
    while ((len = getline(line, MAXLINE)) > 0)
    {
        len = del_space(line, len);
        if (len > 1)
            printf("line length:%d %s", len, line);
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

void copy(char to[], char from[])
{
    int i;

    i = 0;
    while ((to[i] = from[i]) != '\0')
        ++i;

    return;
}

int del_space(char s[], int len)
{
    int i;
    
    if (len == 1)
        return 1;

    for (i = len - 2; i >= 0; --i)
    {
        if (s[i] == '\t' || s[i] == ' ')
        {
            s[i] = '\n';
            s[i + 1] = '\0';
        }
        else
        {
            i = i + 1;
            break;
        }
    }

    return i + 1;
}
