for i in range(int(input())):
	n,a = map(int,input().split())
	n,a = max(n,a),min(n,a)
	c=0
	while a<n:
		a = a*8
		c+=1
	if a==n or a//4 ==n or a//2==n:
		print(c)
	else:
		print (-1)