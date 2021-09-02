# to understand 
# def rec(i,prv,ar):
#     if(i<0):
#         return 0
#     else:
#         ans = 10**7
#         if(ar[i]==3):
#             for j in range(3):
#                 if(j!=prv):
#                     if(j==0 ):
#                         ans=min(ans , 1+rec(i-1,j,ar))
#                     else:
#                         ans = min(ans , rec(i-1,j,ar))
#         else:
#             if(ar[i]==0):
#                 ans=min(ans , 1+rec(i-1,0,ar))
#             elif ar[i]==1:
#                 if(ar[i]==prv):                
#                     ans=min(ans , 1+rec(i-1,0,ar)) 
#                 else:
#                     ans=min(ans , rec(i-1,1,ar))
#             else:
#                 if(ar[i]==prv):             
#                     ans=min(ans , 1+rec(i-1,0,ar))
#                 else:
#                     ans=min(ans ,rec(i-1,2,ar))
#         return ans

def fun(n,ls):
    dp = [[10**7 for i in range(n)] for i in range(3)]
    for i in range(n):
        for j in range(3):
            val=ls[i]
            if (i==0):
                if(val==0 or val==j):
                    dp[j][i]=1
                else:
                    dp[j][i]=0
            else:
                if (val==3):
                    ans=10**7
                    for k in range(3):
                        if(k!=j):
                            if(k==0):
                                ans=min(ans , 1+dp[k][i-1])
                            else:
                                ans=min(ans , dp[k][i-1])
                    dp[j][i]=ans
                else:
                    ans = 10**7
                    if(val==0):
                        ans=min(ans , 1+dp[0][i-1])
                    elif val==1:
                        if(val==j):                
                            ans=min(ans , 1+dp[0][i-1]) 
                        else:
                            ans=min(ans , dp[1][i-1])
                    else:
                        if(val==j):             
                            ans=min(ans , 1+dp[0][i-1])
                        else:
                            ans=min(ans , dp[2][i-1])
                    dp[j][i]=ans
    print(dp[0][n-1])


T=1
for i in range(T):
    n=int(input())
    ls= list(map(int, input().split()))
    fun(n,ls)