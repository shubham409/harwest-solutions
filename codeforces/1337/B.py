for _ in range(int(input())):
    x, n, m = map(int, input().split())
    for _ in range(n):
        x = min(x, x//2+10)
    print('NO' if x > 10*m else 'YES')