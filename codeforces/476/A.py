def fun(ls):
    n,m=ls
    mx=n
    mn=n//2
    if(m>n):
        print(-1)
        return
    start=0
    if(n%2==0):
        start=n//2
    else:
        start=(n//2)+1
    for i in range(start ,n+1):
        if(i%m==0):
            print(i)
            return
    print(-1)


    
# T = int(input())
T = 1
for i in range(T):
    # var=input()
    # val=int(input())
    # st=input()
    # ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls)