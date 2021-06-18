def fun(ls):
    sm=sum(ls)
    if(sm<n):
        print(1)
        return
    if(sm==n):
        print(0)
        return
    if(sm>n):
        print(sm-n)





T = int(input())
# T=1
for i in range(T):
    n=int(input())
    # st=input()
    # ts=input()
    # ks= list(map(int, input().split()))    
    # ls= list(map(int, input().split()))    
    ls= list(map(int, input().split()))    
    fun(ls)