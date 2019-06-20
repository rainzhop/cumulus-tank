/*
 * 用read、write、open和close系统调用代替标准苦衷功能等价的函数，
 * 重写第7章的cat程序，并通过实验比较两个版本的相对执行速度。
 */

#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>

int main(int argc, char **argv)
{
    char buf[BUFSIZ];
    int fd, n;

    if (argc == 1)
    {
        n = read(0, buf, BUFSIZ);
        write(1, buf, n);
    }

    while (--argc > 0)
    {
        fd = open(*(++argv), O_RDONLY, 0);
        n = read(fd, buf, BUFSIZ);
        write(1, buf, n);
        close(fd);
    }
    
    return 0;
}
