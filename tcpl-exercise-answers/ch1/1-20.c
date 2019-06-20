/*
 * 编写程序detab，将输入中的制表符替换成适当数目的空格，
 * 使空格充满到下一个制表符终止位的地方。
 */

#include <stdio.h>

#define MAXLINE 1000
#define ts 8

int getline(char line[], int maxline);
int detab(char s[], int len);

int main()
{
    int len;
    char line[MAXLINE];

    while ((len = getline(line, MAXLINE)) > 0)
    {
        detab(line, len);
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

int detab(char s[], int len)
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
