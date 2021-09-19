def fun(ls,n):
    if ls[-1]==0:
        print(*[i for i in range(1,n+2)])
    else:
        if n==1 and ls[0]==1:
            print(2,1)
            return
        ans=[]
        possible=False
        last_value=None
        for i in range(n-1):
            index_stw1 = i+1
            cur_val = ls[i]
            next_val= ls[i+1]
            if( cur_val ==0 and next_val==1 ):
                ans.append(index_stw1)
                ans.append(n+1)
                last_value= index_stw1+1
                possible=True
                break
            ans.append(index_stw1)
        if(possible):
            ans.extend(range(last_value,n+1))
            print(*ans)
            return
        if ls[0]==1:
            print(*([n+1]+[i for i in range(1,n+1)]))
        else:
            print(-1)
 
 
    
 
 
T = int(input())
# T=1
for i in range(T):
    # st= input()
    n = int(input())
    ls = list(map(int, input().split()))
    # ls = list(map(int, input().split()))
    fun(ls,n)

