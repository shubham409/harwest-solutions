n=int(input())
for _ in range(n):
	arr=list(map(int,list(input())))
	s=sum(arr)
	d2=False
	d0=False
	for i in arr:
		if d0==False and i==0:
			d0=True
		elif i%2==0:
			d2=True
	if d0 and s%3==0 and d2:
		print("red")
	else:
		print("cyan")
