for i in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	for j in range(0, len(a), 2):
		print(-a[j+1], a[j], end=" ")
	print()
