a = 'abcdefghijklmnopqrstuvwxyz'
b = 'pvwdgazxubqfsnrhocitlkeymj'

trans = str.maketrans(b, a)

src = 'Wxgcg txgcg ui p ixgff, txgcg ui p epm. I gyhgwt mrl lig txg ixgff wrsspnd tr irfkg txui hcrvfgs, nre, hfgpig tcm liunz txg crt13 ra "ixgff" tr gntgc ngyt fgkgf.'

print(src.translate(trans))
