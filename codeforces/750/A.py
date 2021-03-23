def fun(ls):
    n,t=ls
    t=240-t
    ans=0
    count=0
    for i in range(1,n+1):
        if(ans+i*5<=t):
            ans+=i*5
            count=i
    print(count)

ls = list(map(int, input().split()))
fun(ls)