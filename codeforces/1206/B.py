def fun(ls):
    zero=False
    st=list(sorted(ls))
    coins=0
    proudct=1
    for i in ls:
        if(i<0):
            proudct*=-1
            coins+=(-(1+i))
        if(i>0):
            proudct*=1
            coins+=(i-1)

        if(i==0):
            proudct*=1
            coins+=1
            zero=True
    if(proudct==-1):
        if(zero):
            print(coins)
            return
        print(coins+2)
    else:
        print(coins)




    

T = int(input())
for i in range(1):
    # var=input()
    # st=input()
    # val=int(input())
    # ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls)
    