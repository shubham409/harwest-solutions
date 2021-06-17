for i in range(int(input())):
    n,m = map(int,input().split())
    print(min(sum([int(s) for s in input().split()]),m))
