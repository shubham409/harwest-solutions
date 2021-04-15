n=int(input())
a=sorted(list(map(int,input().split())))
m=0
for i in range(1,n,2):
    m+=a[i]-a[i-1]
print(m)