def fun(ls):
    n,m=ls
    print(n+((n-1)//(m-1)))


for i in range(1):
    ls= list(map(int, input().split()))
    fun(ls)