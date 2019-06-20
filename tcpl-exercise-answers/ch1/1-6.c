/*
 * 验证表达式getchar() != EOF的值是0还是1。
 */

#include <stdio.h>

int main()
{
    while(1)
        printf("getchar() != EOF的值：%d\n", getchar() != EOF);

    return 0;
}
