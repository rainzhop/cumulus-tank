/*
 * 编写函数reverse(s)，将字符串s中的字符顺序颠倒过来。
 * 使用该函数编写一个程序，每次颠倒一个输入行中的字符顺序。
 */

#include <stdio.h>

#define MAXLINE 1000

int getline(char line[], int maxline);
void reverse(char s[]);

int main()
{
    int len;
    char line[MAXLINE];

    while ((len = getline(line, MAXLINE)) > 0)
    {
        reverse(line);
        printf("%s", line);
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

void reverse(char s[])
{
    int i, j;
    char c;
    i = 0;
    j = 0;

    while (s[j] != '\n') /* 此处由于是颠倒输入行的字符顺序，所以以'\n'作为颠倒的结束位置 */
        ++j;
    j--;

    while (i < j)
    {
        c = s[i];
        s[i++] = s[j];
        s[j--] = c;
    }
}
