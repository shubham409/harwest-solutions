def fun(ls,ms):
    ls=sorted(ls)
    ans=0
    count=0
    for i in ls:
        if(i<0):
            ans+=i
            count+=1
        if(count>=ms[1]):
            break
    print(abs(ans))

    
# T = int(input())
T = 1
for i in range(T):
    # var=input()
    # val=int(input())
    # st=input()
    ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls,ms)