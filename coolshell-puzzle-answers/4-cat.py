f = open("mess.txt", 'r')

mess = f.read()

def ispal(s):
    a = []
    for i in range(0, len(s)):
        a.append(s[-i-1])
    t = ''.join(a)
    if t == s:
        return 1
    return 0

pal = []
for i in range(0, len(mess) - 4):
    if ispal(mess[i:i+5]):
        pal.append(mess[i:i+5])

res = []
for p in pal:
    a = p[0]
    b = p[1]
    c = p[2]
    if c.islower():
        if (a.isdigit() and b.isupper()) or (a.isupper() and b.isdigit()):
            res.append(p)

print(''.join(p[2] for p in res))






