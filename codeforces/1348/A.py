def fun(ls):
    T=ls
    ls=[(2**i)for i in range(1,T+1)]
    n=(T//2)-1
    last=ls[-1]
    mid=ls[n]
    sum1=sum(ls[:n])+last
    sum2=sum(ls[n:-1])
    print(sum1-sum2)

T = int(input())
for i in range(T):
    v=(int(input()))
    fun(v)