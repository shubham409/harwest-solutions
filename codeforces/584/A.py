n,m=map(int,input().split())
p=len(str(m))
print (-1 if p>n else m*(10**(n-p)))