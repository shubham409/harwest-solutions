n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
x=sum(1 for i in range(n) if a[i]>b[i])
y=sum(1 for i in range(n) if a[i]<b[i])
if x==0: print(-1)
else:
	print(y//x+1)
