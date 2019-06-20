/*
 * 编写一个程序打印摄氏温度转换为相应华氏温度的转换表。
 */

#include <stdio.h>

int main()
{
    float fahr, celsius;
    int lower, upper, step;

    lower = -90;
    upper = 90;
    step = 15;

    printf("摄氏温度-华氏温度对照表\n");

    celsius = lower;
    while (celsius <= upper)
    {
        fahr = (9.0 / 5.0) * celsius + 32.0;
        printf("%3.0f %6.1f\n", celsius, fahr);
        celsius = celsius + step;
    }

    return 0;
}
