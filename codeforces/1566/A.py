from math import floor,gcd,ceil


def fun(ls):
    n,sm= ls
    total =sm
    rem=None
    if(n==1):
        print(total)
        return
    if(n==2):
        print(total//2)
        return
    if(n%2!=0):
        rem=ceil(n/2)
    else:
        rem=(n//2)+1
    print(total//rem)


T = int(input())
for i in range(T):
    ls = list(map(int, input().split()))
    fun(ls)
