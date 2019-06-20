cha = 'A'

chalist = []
numlist = []
chadic = {}
for i in range(0, 26):
    C = chr(ord(cha)+i)
    chalist.append(C)
    numlist.append(i+1)
    chadic[C] = i+1

up = "COOLSHELL"
down = "SHELL"

def str2num(s):
    n = 0
    for i in range(0, len(s)):
        n = n + chadic[s[i]] * (26 ** (len(s)-i-1))
    return n

upn = str2num(up)
downn = str2num(down)

res = int(upn/downn)

def num2str(n):
    s = ''
    while(n != 0):
        a = n % 26
        s = chr(ord('A') + a - 1) + s
        n = int(n / 26)
    return s

print(num2str(res))

        
