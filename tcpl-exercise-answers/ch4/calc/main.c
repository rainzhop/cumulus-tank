#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "calc.h"

#define MAXOP 100

int main(void)
{
    int type, ans_flag;
    double op1, op2, ans;
    char s[MAXOP], nl[1];

    while ((type = getop(s, nl)) != EOF && nl[0] != EOF)
    {
        switch (type)
        {
            case NUMBER:
                push(atof(s));
                break;
            case '+':
                push(pop() + pop());
                break;
            case '*':
                push(pop() * pop());
                break;
            case '-':
                op2 = pop();
                push(pop() - op2);
                break;
            case '/':
                op2 = pop();
                if(op2 != 0.0)
                    push(pop() / op2);
                else
                    printf("error: zero divisor\n");
                break;
            case '%':
                op2 = pop();
                if((int)op2 != 0)
                    push((int)pop() % (int)op2);
                else
                    printf("error: zero divisor\n");
                break;
            case SIN:
                push(sin(pop()));
                break;
            case EXP:
                push(exp(pop()));
                break;
            case POW:
                op2 = pop();
                op1 = pop();
                if (op1 == 0 && op2 <= 0)
                    printf("exponent should be positive.\n");
                else if (op1 < 0)
                    push(pow(op1, (int)op2));
                else
                    push(pow(op1, op2));
                break;
            case ANS:
                printf("the last answer: %f\n", ans);
                break;
            case UNKNOWN:
                printf("error: unknown command %s\n", s);
                break;
            default:
                break;
        }
        if (nl[0] == '\n')
        {
            ans = pop();
            printf("the current answer: %f\n", ans);
            nl[0] = 0;
        }
    }

    return 0;
}
