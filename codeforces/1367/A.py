# from pythonchef import *
def func(st):
	ans=''
	ans+=st[0]
	for i in  range(1,len(st),2):
		ans+=st[i] 
	print(ans)

T=int(input())	
for _ in range(T):
	st=input()
	func(st)