for i in range(int(input())):
    n = int(input())
    for j in range(2):
        print(*sorted(list(map(int, input().split()))))