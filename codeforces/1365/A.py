for _ in range(int(input())):
    n, m = map(int, input().split())
    a, b = {}, {}
    for i in range(n):
        for j, x1 in enumerate(input().split()):
            if '1' == x1:
                a[i] = 1
                b[j] = 1
    x = min(n - len(a), m - len(b))
    print('Ashish' if x % 2 else 'Vivek')