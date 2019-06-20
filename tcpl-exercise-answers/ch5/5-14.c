/*
 * 修改排序程序，使它能处理-r标记。
 * 该标记表明，以逆序（递减）方式排序。
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXLINE 1000

int getline(char line[], int maxline);
void sort(void *v[], int left, int right, int (*comp)(void *, void *), int r_flag);
void swap(void *v[], int i, int j);
int numcmp(char *s1, char *s2);

char linebuf[10000];

int main(int argc, char **argv)
{
    int len, line_num, i;
    char *lineptr[MAXLINE];
    char *p = linebuf;
    char line[MAXLINE];

    char *pav;
    int n_flag, r_flag, f_flag, d_flag;
    n_flag = 0;
    r_flag = 1;
    f_flag = 0;
    d_flag = 0;

    while (--argc > 0)
    {
        if ((*(++argv))[0] != '-')
        {
            printf("input para error.\n");
            return -1;
        }

        for (pav = *argv + 1; *pav != '\0'; ++pav)
        {
            switch (*pav)
            {
                case 'n':
                    n_flag = 1;
                    break;
                case 'r':
                    r_flag = -1;
                    break;
                default:
                    printf("input para error.\n");
                    return -1;
            }
        }
    }

    i = 0;
    while ((len = getline(line, MAXLINE)) > 0)
    {
        strcpy(p, line);
        lineptr[i++] = p;
        p += len + 1;
    }
    line_num = i;

    if (n_flag == 1)
        sort((void **)lineptr, 0, line_num - 1, (int (*)(void *, void *))numcmp, r_flag);
    else 
        sort((void **)lineptr, 0, line_num - 1, (int (*)(void *, void *))strcmp, r_flag);

    for (i = 0; i < line_num; ++i)
        printf("%s", lineptr[i]);
    return 0;
}

void sort(void *v[], int left, int right, int (*comp)(void *, void *), int r_flag)
{
    int i, last;
    void swap(void *v[], int, int);

    if (left >= right)
        return;
    swap(v, left, (left + right)/2);
    last = left;
    for (i = left + 1; i <= right; i++)
        if (r_flag * (*comp)(v[i], v[left]) < 0)
            swap(v, ++last, i);
    swap(v, left, last);
    sort(v, left, last-1, comp, r_flag);
    sort(v, last + 1, right, comp, r_flag);
}

int numcmp(char *s1, char *s2)
{
    double v1, v2;

    v1 = atof(s1);
    v2 = atof(s2);
    if (v1 < v2)
        return -1;
    else if (v1 > v2)
        return 1;
    else
        return 0;
}

void swap(void *v[], int i, int j)
{
    void *temp;
    temp = v[i];
    v[i] = v[j];
    v[j] = temp;
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
