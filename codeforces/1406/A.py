for _ in range(int(input())):
    n, lis, a, b = int(input()), sorted(list(map(int, input().split()))), 0, 0
    for i in lis:
        if a == i:
            a += 1
        elif b == i:
            b += 1
    print(a + b)