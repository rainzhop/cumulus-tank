/*
 * 编写一个程序，比较两个文件并打印它们第一个不相同的行。
 */

#include <stdio.h>
#include <string.h>

#define MAX_LINE_LEN 1000

int main()
{
    int i = 1;

    FILE *f1 = fopen("file1.txt", "r");
    FILE *f2 = fopen("file2.txt", "r");
    char line1[MAX_LINE_LEN];
    char line2[MAX_LINE_LEN];

    while (feof(f1) == 0 && feof(f2) == 0)
    {
        fgets(line1,MAX_LINE_LEN, f1);
        fgets(line2,MAX_LINE_LEN, f2);
        if (strcmp(line1, line2) != 0)
        {
            printf("file1 %d: %s", i, line1);
            printf("file2 %d: %s", i, line2);
            return 0;
        }
        ++i;
    }
    
    printf("each line in file1 is the same as the one in file2.\n");
    return 0;
}
