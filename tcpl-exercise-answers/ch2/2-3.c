/*
 * 编写函数htoi(s)，把由十六进制数字组成的字符串（包含可选的前缀0x或0X）转换为与之等价的整形值。
 * 字符串中允许包含的数字包括：0~9、a~f以及A~F。
 */

/* 仅支持正数 */
int htoi(char s[])
{
    int i, n;
    n = 0;

    if (s[0] != '0' || (s[1] != 'x' && s[1] != 'X'))
        return -1;

    for (i = 2; s[i] != '\0'; ++i)
    {
        if (s[i] >= '0' && s[i] <= '9')
            n = n * 16 + (s[i] - '0');
        else if (s[i] >= 'a' && s[i] <= 'f')
            n = n * 16 + (s[i] - 'a' + 10);
        else if (s[i] >= 'A' && s[i] <= 'F')
            n = n * 16 + (s[i] - 'A' + 10);
        else
            return -1;
    }

    return n;
}
