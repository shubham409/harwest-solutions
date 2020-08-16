def fun(l,n):
	mx = max(l)
	mn = min (l)
	ls=l
	num = mx- mn
	odd = [mx-i for i in ls]
	evn = [num - i for i in odd]
	if n%2==0:
		print(*evn)
	else:
		print(*odd)

T=int(input())
for _ in range(T):
    i= (input().split())
    i=list(map(int,i))
    n=i[1]
    x =input().split(" ")
    x=list(map(int,x))
    fun(x,n)