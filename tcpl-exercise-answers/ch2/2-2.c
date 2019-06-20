for (i = 0; i < lim - 1 && (c = getchar()) != '\n' && c != EOF; ++i)
    s[i] = c;

/*
 * 在不使用运算符&&或||的条件下编写一个与上面的for循环语句等价的循环语句。
 */

for (i = 0; i < lim - 1; ++i)
{
    c = getchar();

    if (c == '\n')
        break;
    if (c == EOF)
        break;

    s[i] = c;
}
