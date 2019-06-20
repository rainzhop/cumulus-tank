import urllib.request
uri = 'http://fun.coolshell.cn/n/'

def getpage(c, n = 2014):
    for _ in range(0, c):
        u = urllib.request.urlopen(uri + str(n))
        page = u.read()
        if page.isdigit():
            n = eval(page)
            print(n)
        else:
            print(page)
            return

getpage(500, n = 2014)
