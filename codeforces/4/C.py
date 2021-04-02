x = int(input())
a = {}
for i in range(x):
	s = input()
	if(s in a):
		a[s]+=1
		print(s+str(a[s]))
	else:
		a[s]=0
		print("OK")
