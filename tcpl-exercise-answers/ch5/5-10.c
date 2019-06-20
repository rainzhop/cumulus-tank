/*
 * 编写程序expr，以计算从命令行输入的逆波兰表达式的值，
 * 其中每个运算符或操作数用一个单独的参数表示。
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    double num[100];
    char *endp;
    char *blank = "";
    char op;
    int top = 0;
    int i;
    double op1, op2;

    if (argc == 1)
    {
        printf("input para error.\n");
        return -1;
    }

    for (i = 1; i < argc; ++i)
    {
        op1 = strtod(argv[i], &endp);
        if (strcmp(endp, blank) == 0)
        {
            num[top++] = op1;
            continue;
        }

        if(top < 2)
        {
            printf("input para error.\n");
            return -1;
        }

        if (strcmp(argv[i], "+") == 0)
        {
            op2 = num[--top];
            op1 = num[--top];
            num[top++] = op1 + op2;
        }
        if (strcmp(argv[i], "-") == 0)
        { 
            op2 = num[--top];
            op1 = num[--top];
            num[top++] = op1 - op2;
        }
        if (strcmp(argv[i], ".") == 0)
        { 
            op2 = num[--top];
            op1 = num[--top];
            num[top++] = op1 * op2;
        }
        if (strcmp(argv[i], "/") == 0)
        { 
            op2 = num[--top];
            op1 = num[--top];
            num[top++] = op1 / op2;
        }
    }

    if (top == 1)
        printf("result is %f\n", num[0]);
    else
        printf("input para error.\n");

    return 0;
}
