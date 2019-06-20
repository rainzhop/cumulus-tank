/*
 * 编写一个函数rightrot(x, n)，该函数返回将x循环右移
 * （即从最右端移出的位将从最左端移入）n（二进制）位后所得到的值。
 */

unsigned int rightrot(unsigned int x, int n)
{
    return (x >> n) | (x << (8 * sizeof(unsigned int) - n));
}
