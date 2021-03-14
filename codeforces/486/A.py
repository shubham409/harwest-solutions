from math import ceil,floor
def fun(n):
    if(n%2==0):
        print(n//2)
    else:
        print(-ceil(n/2))


# T = int(input())
# for i in range(T):
# n = list(map(int, input().split()))
n = int(input())
# ls = list(map(int, input().split()))
# ipt= input()
fun(n)