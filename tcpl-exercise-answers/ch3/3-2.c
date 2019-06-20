/*
 * 编写一个函数escape(s, t)，将字符串t复制到字符串s中，并在复制过程中将换行符，
 * 制表符等不可见字符分别转换为\n、\t等相应的可见的转义字符序列。
 * 要求使用switch语句。
 */

void escape(char s[], char t[])
{
    int i = 0;
    int j = 0;
    
    while (s[i] != '\0')
    {
        switch (t[j])
        {
            case '\n':
                s[i++] = '\\';
                s[i++] = 'n';
                break;
            case '\t':
                s[i++] = '\\';
                s[i++] = 't';
                break;
            case '\0':
                return;
            default:
                s[i++] = t[j];
                break;
        }
        ++j;
}

    return;
}
