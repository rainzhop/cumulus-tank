/*
 * 在求对二的补码时，表达式x &= （x - 1)可以删除x中最右边值位1的一个二进制位。
 * 用这一方法重写bitcount函数，以加快其执行速度。
 */

int bitcount(unsigned x)
{
    int n = 0;

    while (x != 0)
    {
        x &= (x - 1);
        ++n;
    }
    
    return n;
}
