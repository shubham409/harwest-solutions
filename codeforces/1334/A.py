t=int(input())
for _ in range(t):
	n = int(input())
	a, b = 0,0
	res = True
	for i in range(n):
		c, d = map(int, input().split())
		if (c-a < d-b) or (a>c or b>d): res=False
		a,b = c,d
	print(['NO', 'YES'][res])