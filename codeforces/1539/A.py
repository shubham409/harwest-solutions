for _ in range(int(input())):
	n,x,t=map(int,input().split())
	s=min(n-1,t//x)
	print([s,(s*(s-1)//2)+s*(n-s)][s!=0])