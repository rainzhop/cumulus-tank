/*
 * 编写程序entab，将空格替换位最少数量的制表符和空格，但要保持单词之间的间隔不变。
 */

#include <stdio.h>

#define MAXLINE 1000
#define ts 8

int getline(char line[], int maxline);
int entab(char s[], int len);

int main()
{
    int len;
    char line[MAXLINE];

    while ((len = getline(line, MAXLINE)) > 0)
    {
        entab(line, len);
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

int entab(char s[], int len)
{
    char tmp[MAXLINE] = { 0 };
    int i, j, space_num;

    for (i = 0; i < len; ++i)
        tmp[i] = s[i];

    space_num = 0;
    j = 0;
    for (i = 0; i < len; ++i)
    {
        if (space_num % ts == 0 && space_num > 0)
        {
            s[j++] = '\t';
            space_num = 0;
        }

        if (tmp[i] == ' ')
            ++space_num;
        else
        {
            while (space_num > 0)
            {
                s[j++] = ' ';
                --space_num;
            }
            s[j++] = tmp[i];
        }
    }
    s[j] = '\0';

    return j;
}
