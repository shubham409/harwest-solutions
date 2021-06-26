R=lambda:map(int,input().split())
s=sorted
n,k,x=R()
a=s(R())
for u in s(max(v-u,x)for u,v in zip(a,a[1:])):
 k+=-u//x+1
 if k<0:break
 n-=1
print(n)
