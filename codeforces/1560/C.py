from math import floor, gcd,ceil,sqrt


def fun(n):
    prv =  floor(sqrt(n))
    if(prv*prv == n):
        print(prv,1)
    else:
        col = prv+1
        start=(prv*prv)
        for i in range(col):
            start=start+1
            if(start==n):
                print(i+1 , col)
                return
        start-=1
        for i in range(col,0,-1):
            start=start+1
            if(start==n):
                print(col ,i)
                return
        print(-1)

T = int(input())
for i in range(T):
    n=int(input())
    fun(n)
    