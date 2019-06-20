/*
 * 编写函数expand(s1, s2)，将字符串s1中类似于a-z一类的速记符号
 * 在字符串s2中扩展为等价的完整列表abc…xyz。该函数可以处理大小写字母和数字，
 * 并可以处理a-b-c、a-z0-9与-a-z等类似的情况。作为前导和尾随的-字符原样排印。
 */

/* 调用该函数时应保证s2空间足够大，这里只实现基本功能 */
void expand(char s1[], char s2[])
{
    int i = 0;
    int j = 0;
    char c;
    char start, end;

    while ((c = s1[i]) != '\0')
    {
        if (s1[i + 1] == '-')
        {
            start = c;
            end = s1[i + 2];
            if (start >= 'a' && end <= 'z' && start < end)
            {
                for (c = start; c <= end; ++c)
                    s2[j++] = c;
                i = i + 2;
            }
            else if (start >= 'A' && end <= 'Z' && start < end)
            {
                for (c = start; c <= end; ++c)
                    s2[j++] = c;
                i = i + 2;
            }
            else if (start >= '0' && end <= '9' && start < end)
            {
                for (c = start; c <= end; ++c)
                    s2[j++] = c;
                i = i + 2;
            }
            else
                s2[j++] = c;
        }
        else
            s2[j++] = c;
        ++i;
    }
    s2[j] = '\0';

    return;
}
