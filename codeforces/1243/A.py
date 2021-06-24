for _ in range(int(input())):
	n = int(input())
	l = sorted(list(map(int,input().split())))
	while l[0]<n:
		l.pop(0)
		n -= 1
	print(n)