def fun(ls,n):
    ans=0
    for i in ls:
        ans= ans | i
    if(ans):
        print("HARD")
    else:
        print("EASY")


    
# T = int(input())
for i in range(1):
    # var=input()
    # st=input()
    val=int(input())
    # n,h= list(map(int, input().split()))
    ls = list(map(int, input().split()))
    fun(ls,val)
    # fun(st,var)
