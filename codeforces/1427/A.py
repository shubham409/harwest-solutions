for _ in range(int(input())):
	n = int(input())
	l = [int(i) for i in input().split()]
	if sum(l) == 0:
		print('NO')
	else:
		print('YES')
		if sum(l) < 0:
			l.sort()
			print(*l)
		else:
			l.sort(reverse = True)
			print(*l)