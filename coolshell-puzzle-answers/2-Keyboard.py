strdravok = "'  ,  .  p  y  f  g  c  r  l  /  =  \  a  o  e  u  i  d  h  t  n  s  -  ;  q  j  k  x  b  m  w  v  z [ ]"
strqwerty = "q  w  e  r  t  y  u  i  o  p  [  ]  \  a  s  d  f  g  h  j  k  l  ;  '  z  x  c  v  b  n  m  ,  .  / - ="

dravok = {}

for a in range(0, len(strdravok)):
    if strdravok[a] != ' ':
        dravok[strdravok[a]] = strqwerty[a]

strpuzzle = "macb() ? lpcbyu(&gbcq/_ \ 0 2 1 %ocq\ 0 1 2 \ 0_=w(gbcq)/_dak._=}_ugb_[0q60)s+"

ans = []

for c in strpuzzle:
    if c in strdravok and c != ' ':
        ans.append(dravok[c])
    else:
        ans.append(c)

res = ''.join(ans)

strdravok = '"  <  >  P  Y  F  G  C  R  L  ?  +  |  A  O  E  U  I  D  H  T  N  S  _  :  Q  J  K  X  B  M  W  V  Z { } '
strqwerty = 'Q  W  E  R  T  Y  U  I  O  P  {  }  |  A  S  D  F  G  H  J  K  L  :  "  Z  X  C  V  B  N  M  <  >  ? _ + '

for a in range(0, len(strdravok)):
    if strdravok[a] != ' ':
        dravok[strdravok[a]] = strqwerty[a]

strpuzzle = res

ans = []

for c in strpuzzle:
    if c in strdravok and c != ' ':
        ans.append(dravok[c])
    else:
        ans.append(c)
            
res = ''.join(ans)
print(res)
