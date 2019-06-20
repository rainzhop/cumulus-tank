/* 
 * 编写一个程序，打印输入中各个字符出现频度的直方图。
 */

#include <stdio.h>

int main()
{
    char c;
    int i, j;
    int char_freq[128] = {0};

    while ((c = getchar()) != EOF)
        ++char_freq[c];

    for (i = 0; i < 128; ++i)
    {
        if (char_freq[i] == 0)
            continue;

        if (i > 32)
            printf("      %3c ", i);
        else
            printf("ascii:%3d ", i);

        for (j = 0; j < char_freq[i]; ++j)
            printf("*");

        printf("\n");
    }

    return 0;
}
