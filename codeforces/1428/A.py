for _ in range(int(input())):
	a,b,c,d=map(int,input().split())
	e,f=abs(a-c),abs(b-d)
	if e and f:
		print(e+f+2)
	else:
		print(e+f)