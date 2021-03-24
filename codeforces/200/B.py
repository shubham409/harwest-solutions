from math import ceil,floor
def fun(ls,n):
    ans=0.0
    for i in ls:
        ans+=(i/100)
    print("%.6f"%((ans/n)*100))

n = int(input())
ls = list(map(int, input().split()))
fun(ls,n)