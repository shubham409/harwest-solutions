def fun(ls):
    start, end = ls
    if end <= start:
        print(start - end )
    else:
        ans = 0 
        while(start != end ):

            if end % 2 ==0 and end > start:
                end /=2 
                ans += 1  
            else:
                end+=1
                ans+=1

        print(ans)







# T = int(input())
T = 1
for i in range(T):
    # st=input()
    # n=int(input())
    # n=int(input())
    # n=int(input())
    ls= list(map(int, input().split()))
    # lt= list(map(int, input().split()))
    # fun(ls,n)
    fun(ls)