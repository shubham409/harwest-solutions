a,b= map(int,input().split())
l=list(map(int,input().split()))
c=1
for i in range(1, a):
	if l[i]-l[i-1] <=b:
		 c+=1
	else: 
		c=1
print(c)