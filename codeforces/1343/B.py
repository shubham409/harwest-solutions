t = int(input())
for _ in range(t):
	n = int(input())
	if n%4 != 0:
		print("NO")
	else:
		n=n//2
		print("YES")
		for i in range(1,n+1):
			print(i*2,end=" ")
		for i in range(1,n):
			print(i*2-1,end =" ")
		print(3*n-1)