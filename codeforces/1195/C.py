import sys
from collections import Counter

# to understand
# def reccursion(i , row , first ,second):
#     if(i==0):
#         if(row==0):
#             return first[0]
#         else:
#             return second[0]

#     elif i==-1:
#         return 0
#     else:
#         if(row==0):
#             return first[i]+max(reccursion(i-1,1,first,second),reccursion(i-2,1,first,second))
#         else:
#             return second[i]+max(reccursion(i-1,0,first,second),reccursion(i-2,0,first,second))

def fun(ls,lt,n):
    first = ls
    second =lt
    dp=[[j for j in range(10**6)]for i in range(2)]
    
    for i in range(n):
        for j in range(2):
            # print(i,j)
            if(i==0):
                if(j==0):
                    dp[j][i] = first[0]
                else:
                    dp[j][i] = second[0]

            elif (i==1):
                if(j==0):
                    dp[j][i] = first[1]+second[0]
                else:
                    dp[j][i] = second[1]+first[0]
            else:
                if(j==0):
                    dp[j][i]= first[i]+max(dp[1][i-1],dp[1][i-2])
                else:
                    dp[j][i]= second[i]+max(dp[0][i-1],dp[0][i-2])
    print(max(dp[0][n-1],dp[1][n-1]))


T=1
for i in range(T):
    n=int(input())
    lt= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls,lt,n)