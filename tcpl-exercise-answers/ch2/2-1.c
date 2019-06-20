/*
 * 编写一个程序以确定分别由signed及unsigned
 * 限定的char、short、int与long类型变量的取值范围。
 */

#include <stdio.h>
#include <limits.h>

int main()
{
    printf("---------- 取值范围 ----------\n");
    printf("  signed char : %12d ~ %d\n", SCHAR_MIN, SCHAR_MAX);
    printf("  signed short: %12d ~ %d\n", SHRT_MIN, SHRT_MAX);
    printf("  signed int  : %12d ~ %d\n", INT_MIN, INT_MAX);
    printf("  signed long : %12d ~ %d\n", LONG_MIN, LONG_MAX);
    printf("unsigned char : %12d ~ %u\n", 0, UCHAR_MAX);
    printf("unsigned short: %12d ~ %u\n", 0, USHRT_MAX);
    printf("unsigned int  : %12d ~ %u\n", 0, UINT_MAX);
    printf("unsigned long : %12d ~ %u\n", 0, ULONG_MAX);

    return 0;
}
