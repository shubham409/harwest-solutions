for _ in range(int(input())):
	n, k = map(int, input().split())
	print(['YES', 'NO'][(n%2 != k%2 or n < k*k)])