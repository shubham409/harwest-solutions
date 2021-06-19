a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
if e>f:
    n=min(a,d)
    d-=n
    m=min(d,b,c)
else:
    m=min(b,c,d)
    d-=m
    n=min(a,d)
print(n*e+m*f)