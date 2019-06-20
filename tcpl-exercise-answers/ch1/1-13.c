/*
 * 编写一个程序，打印输入中单词长度的直方图。
 * 水平方向的直方图比较容易绘制，垂直方向的直方图则要困难些。
 */

#include <stdio.h>

#define MAX_LEN      12

int main()
{
    char c;
    int cnt, i, j;
    int wn[MAX_LEN + 1 + 1] = {0}; /* 还要额外存放长度为0及长度超过MAX_LEN */

    cnt = 0;
    while ((c = getchar()) != EOF)
    {
        if (c == '\n' || c == ' ' || c == '\t')
        {
            ++(wn[cnt]);
            cnt = 0;
            continue;
        }

        ++cnt;
        if (cnt > MAX_LEN)
            cnt = MAX_LEN + 1;
    }
    ++(wn[cnt]);

    /* 打印水平直方图 */
    printf("输入单词长度水平直方图\n");
    for (i = 1; i <= MAX_LEN + 1; ++i)
    {
        if (i == MAX_LEN + 1)
            printf(">%2d ", MAX_LEN);
        else
            printf("%3d ", i);

        for (j = 0; j < wn[i]; ++j)
            printf("*");

        printf("\n");
    }
    printf("\n");

    /* 打印垂直直方图 */
    printf("输入单词长度垂直直方图\n");
    j = 0;
    for (i = 1; i <= MAX_LEN + 1; ++i)
    {
        if (wn[i] > j)
            j = wn[i];
    }
    
    while(j != 0)
    {
        for (i = 1; i <= MAX_LEN + 1; ++i)
        {
            if (wn[i] < j)
                printf("    ");
            else
                printf("  * ");
        }

        printf("\n");
        --j;
    }

    for (i = 1; i <= MAX_LEN; ++i)
        printf(" %2d ", i);

    printf(">%2d", MAX_LEN);

    return 0;
}
