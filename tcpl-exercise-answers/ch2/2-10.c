/*
 * 重新编写将大写字母转换位小写字母的函数lower，
 * 并用条件表达式替代其中的if-else结构。
 */

char lower(char c)
{
    return (c >= 'A' && c <= 'Z') ? (c - 'A' + 'a') : c;
}
