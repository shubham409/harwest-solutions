import string

st=(string.ascii_uppercase)
dct={st[i]:i for i in range(26)}

st=input()
prv=st[0]
show=True
for i,val in enumerate(st[1:-1]):
    i=i+1
    a=dct.get(prv)
    b=dct.get(val)
    c=dct.get(st[i+1])
    if((a+b)%26!=c):
        print('no')
        show=False
        break
    prv=val
if(show):
    print('yes')




