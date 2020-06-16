# from pythonchef import *
def func(ls):
	even=0
	odd=0
	for i,j in enumerate(ls):
		# print(i,j)
		if (i%2==0):
			if(i%2==j%2):
				# print(even,odd)
				continue
			else:
				even+=1
				# print('evn')
		else:
			if(i%2==j%2):
				# print(even,odd)
				continue
			else:
				odd+=1
				# print('od')
	# print(even,odd)
	if (odd==even):
		print(odd)
	else:
		print(-1)
T=int(input())	
for _ in range(T):
	ip=int(input())
	st=input().split(" ")
	# print(st)
	st=list(map(int,st))
	func(st)