def fun(n):
    ans=0
    if(n==1):
        print(0)
        return
    if n%3!=0:
        print(-1)
        return
    while n%6==0:
        n=n//6
        ans+=1
    while n%3==0:
        n=(n//3)
        ans+=2
    if(n==1):
        print(ans)
    else:
        print(-1)


T = int(input())
for i in range(T):
    v=(int(input()))
    fun(v)