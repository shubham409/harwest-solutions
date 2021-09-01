
import sys
from collections import Counter
# x=10**8
# sys.setrecursionlimit(x)


# to understand
# def reccursion(i,count,dp):
#     if(i==1):
#         return count[1]
#     elif i==0:

#         return 0;
#     else:
#         if(dp[i]==-1):
#             dp[i] = max(count[i]*i+reccursion(i-2,count,dp),reccursion(i-1,count,dp))
#             return dp[i]
#         else:
#             return dp[i]

    
def fun(ls,n):
    dp = [-1 for i in range(10**6)]
    maxx= max(ls)
    ct=dict(Counter(ls))
    count = [ 0 for i in range(maxx+1)]
    for i in range(maxx+1):
        if(ct.get(i)!=None):
            count[i]=ct[i]
    for i in range(maxx+1):
        if(i==0):
            dp[i]=0
        elif (i==1):
            dp[i]=count[1]
        else:
            dp[i] = max(dp[i-2]+count[i]*i , dp[i-1])
    print(dp[maxx])


T=1
for i in range(T):
    n=int(input())
    ls= list(map(int, input().split()))
    fun(ls,n)