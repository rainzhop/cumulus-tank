/*
 * 编写一个统计空格、制表符与换行符个数的程序。
 */

#include <stdio.h>

int main()
{
    char c;
    int cnt_space, cnt_table, cnt_lf;

    cnt_space = 0;
    cnt_table = 0;
    cnt_lf = 0;

    while ((c = getchar()) != EOF)
    {
        if (c == ' ')
            ++cnt_space;
        if (c == '\t')
            ++cnt_table;
        if (c == '\n')
            ++cnt_lf;
    }

    printf("空格个数  ：%d\n", cnt_space);
    printf("制表符个数：%d\n", cnt_table);
    printf("换行符个数：%d\n", cnt_lf);
    
    return 0;
}
