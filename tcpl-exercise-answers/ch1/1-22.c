/*
 * 编写一个程序，把较长的输入行“折”成短一些的两行或多行，
 * 折行的位置在输入行的第n列之前的最后一个非空格后。
 */

#include <stdio.h>

#define MAXLINE 1000
#define ts 8
#define FOLD_COL 40

int getline(char line[], int maxline);
int fold(char s[], int len);

int main()
{
    int len;
    char line[MAXLINE];

    while ((len = getline(line, MAXLINE)) > 0)
    {
        fold(line, len);
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

int fold(char s[], int len)
{
    char tmp[MAXLINE] = { 0 };
    char word[MAXLINE] = { 0 };
    int i, j, k, n_letter, n_col;

    for (i = 0; i < len; ++i)
        tmp[i] = s[i];

    n_letter = 0;
    n_col = 0;
    j = 0;
    for (i = 0; i < len; ++i)
    {
        if (tmp[i] == ' ' || tmp[i] == '\t' || tmp[i] == '\n')
        {
            if (n_letter > 0)
            {
                for (k = 0; k < n_letter; ++k)
                {
                    s[j++] = word[k];
                }
                n_letter = 0;
            }
            s[j++] = tmp[i];

            if (tmp[i] == ' ')
                ++n_col;
            else if (tmp[i] == '\t')
                n_col = n_col - (n_col % ts) + ts;
        }
        else
        {
            word[n_letter++] = tmp[i];
            ++n_col;
        }

        if (n_col == FOLD_COL)
        {
            if (n_letter < 5)
            {
                s[j++] = '\n';
                n_col = 0;
            }
            else
            {
                word[n_letter + 1] = word[n_letter - 1];
                word[n_letter - 1] = '-';
                word[n_letter] = '\n';
                n_letter = n_letter + 2;
                n_col = 1;
            }
        }
    }
    s[j] = '\0';

    return j;
}
