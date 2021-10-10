def fun(f,s,n):
    yes = '0'
    no = '1'
    dp = [[False for i in range(100)]for i in range(2)]
    # print(dp)
    for i in range(n-1,-1,-1):
        if(i==n-1):
            if s[i]==no:
                dp[1][i]=False
                dp[0][i]=False
            else:
                dp[1][i]=True
                if f[i]==yes:
                    dp[0][i]=True
                else:
                    dp[0][i]=False

        else:
            if(s[i]==yes):
                dp[1][i] = (dp[1][i+1] or dp[0][i+1] or dp[0][i])
            if(f[i]==yes):
                dp[0][i]= (dp[0][i+1] or dp[1][i+1] or dp[1][i])
    if(dp[0][0]==True):
        print("YES")
    else:
        print("NO")


T = int(input())
for i in range(T):
    n = int(input())
    f= input()
    s= input()
    fun(f,s,n)

