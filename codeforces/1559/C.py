# if last is 0 then we can just go from 1 to n+1 directly
# if last is 1 we should start with one then travel such that one of te point goes from i to n+1 and then returns to i+1 to continue traversing remaining points
# However there is one case in which we would like to start from n+1 when there is path from n+1 to 1 and then remaining points cause they dont have any edge to go on n+1 from any i

def fun(ls,n):
    if ls[-1]==0:
        print(*[i for i in range(1,n+2)])
    else:
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
for i in range(T):
    n = int(input())
    ls = list(map(int, input().split()))
    fun(ls,n)
