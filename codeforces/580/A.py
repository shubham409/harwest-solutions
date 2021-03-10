def fun(ls):
    count=1
    ans=1
    prv=ls[0]
    for i in ls[1:]:
        if(i<prv):
            ans=max(ans,count)
            count=0
        
        count+=1
        prv=i
        ans=max(ans,count)
    print(ans)

    

T = int(input())
for i in range(1):
    # var=input()
    # st=input()
    # val=int(input())
    # ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls)