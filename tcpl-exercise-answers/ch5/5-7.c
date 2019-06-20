/*
 * 重写函数readlines，将输入的文本行存储到由main函数提供的一个数组中，
 * 而不是存储到调用alloc分配的存储空间中。该函数的运行速度比改写前快多少。
 */

#include <stdio.h>
#include <string.h>

#define MAXLINES 5000
#define MAXLEN 1000
#define MAX_BUF_LEN 100000

char *lineptr[MAXLINES];

int readlines(char *lineptr[], int maxlines, char *buf);
int getline(char s[], int lim);

int main()
{
    char buf[MAX_BUF_LEN] = {0};
    readlines(lineptr, MAXLINES, buf);

    return 0;
}

int readlines(char *lineptr[], int maxlines, char *buf)
{
    int pos;
    int len, nlines;
    char line[MAXLEN];
    pos = 0;
    nlines = 0;
    while ((len = getline(line, MAXLEN)) > 0)
    {
        if (nlines >= maxlines || pos + len > MAX_BUF_LEN)
            return -1;
        else {
            line[len - 1] = '\0';
            strcpy(buf + pos, line);
            lineptr[nlines++] = buf + pos;
            pos += len;
        }
    }
    return nlines;
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
