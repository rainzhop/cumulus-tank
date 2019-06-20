/*
 * 修改打印最长文本行的程序的主程序main，
 * 使之可以打印任意长度的输入行的长度，并尽可能多地打印文本。
 */

#include <stdio.h>

#define MAXLINE 1000

int getline(char line[], int maxline);
void copy(char to[], char from[]);

int main()
{
    int len;
    char line[MAXLINE];

    while ((len = getline(line, MAXLINE)) > 0)
        printf("line length:%d %s", len, line);

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
