def fun(ms,ls):
    x,y=ms
    a,b=ls
    # a single up down
    # b double up down
    if(x==0 and y==0):
        print(0)
        return
    mx,mn=max(x,y),min(x,y)
    if(a>b):
        
        print((mn*b)+(mx-mn)*a)
    else:
        if(2*a>b):
            print((mn*b)+(mx-mn)*a)
        else:
            print((mn+mx)*a)

T = int(input())
for i in range(T):
    ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ms,ls)