a = int(input())
for _ in range(a):
    b = int(input())
    print('7'*(b%2)+'1'*(b//2 - b%2))