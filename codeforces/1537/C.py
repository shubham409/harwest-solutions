def a(n, h):
    h.sort()
    if n == 2:
        return h
    mn = abs(h[0]-h[1])
    ind = 1
    for i in range(1, n):
        if abs(h[i]-h[i-1]) < mn:
            mn = abs(h[i]-h[i-1])
            ind = i
    return h[ind:]+h[:ind]


for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    print(*a(n, h))
