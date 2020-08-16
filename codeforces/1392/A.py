
def fun(l):
	# ar = np.array(l)
	# a0=ar[0]
	# a=ar==a0
	a=[i==l[0] for i in l ]
	for i in a:
		if i == False:
			print(1)
			return 
	print(len(l))





T=int(input())
for _ in range(T):
    i= int(input())
    x=input().split(" ")
    x=list(map(int,x))
    fun(x)