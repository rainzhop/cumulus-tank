#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include "calc.h"

int getop(char s[], char nl[])
{
    char c;
    int i, sl, is_num;

    i = 0;
    while ((c = getch()) != EOF && c != ' ' && c != '\t' && c != '\n')
        s[i++] = c;
    if (c == '\n')
        nl[0] = '\n';
    if (c == EOF)
        nl[0] = EOF;
    s[i] = '\0';

    i = 0;
    sl = strlen(s);
    if (sl == 0)
        return ' ';

    is_num = 1;
    if (sl > 1 && (s[0] == '+' || s[0] == '-'))
        i = 1;
    while (i < sl)
        if (!isdigit(s[i++]))
        {
            is_num = 0;
            break;
        }
    if (is_num == 1)
        return NUMBER;

    if (strcmp(s, "sin") == 0)
        return SIN;
    if (strcmp(s, "exp") == 0)
        return EXP;
    if (strcmp(s, "pow") == 0)
        return POW;
    if (strcmp(s, "ans") == 0)
        return ANS;
    if (strcmp(s, "+") == 0)
        return '+';
    if (strcmp(s, "-") == 0)
        return '-';
    if (strcmp(s, "*") == 0)
        return '*';
    if (strcmp(s, "/") == 0)
        return '/';
    if (strcmp(s, "%") == 0)
        return '%';

    return UNKNOWN;
}
