from math import ceil


def fun(ls,n,k):
    val=n
    p0=ls[0]
    ans=0
    sum_till_previous=ls[0]
    for i in range(1,val):
        # 100(pi) = (p0+....+p[i-1]+x)*k
        # if x -ive forget else add ans and sum so far
        x=(100*(ls[i])/(k))-sum_till_previous
        if(x>0):
            sum_till_previous+=ceil(x)
            ans+=ceil(x)
        sum_till_previous+=ls[i]
    print(ans)

   



    
    

T = int(input())
for i in range(T):
    # var=input()
    # st=input()
    # val=int(input())
    n,k= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls,n,k)