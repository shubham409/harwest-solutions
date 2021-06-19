for _ in range(int(input())):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))

    ans = a[0]
    for i in range(1, n):
        p = min(d//i, a[i])
        ans += p
        d -= p * i
    print(ans)