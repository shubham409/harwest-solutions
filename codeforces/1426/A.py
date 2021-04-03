from math import ceil
def fun(ls):
    n,x=ls
    if(n<=2):
        print(1)
    else:
        n=n-2
        print(ceil(n/x)+1)
T = int(input())
for i in range(T):
    ls= list(map(int, input().split()))
    fun(ls)