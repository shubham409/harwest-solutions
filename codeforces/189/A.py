# def reccursion(n,a,b,c):
#     if(n==0):
#         return 0

#     elif n<0:
#         return -10**9

#     else:
#         return 1+max(reccursion(n-a,a,b,c),reccursion(n-b,a,b,c),reccursion(n-c,a,b,c))

def fun(ls):
    n,*ls=ls
    ls=sorted(ls)
    a,b,c=ls
    dp=[0 for i in range(n+1)]
    for i in range(n+1):
        if(i==0):
            dp[i]=0
            continue
        else:
            if i>=c:
                dp[i]=1+max(dp[i-a],dp[i-b],dp[i-c])
            elif i>=b:
                dp[i]=1+max(dp[i-a],dp[i-b])
            elif i>=a:
                dp[i]=1+dp[i-a]
            else:
                dp[i]=-10**9
    print(dp[n])



    
    
        
    
    

# T = int(input())
T=1
for i in range(T):
    # n,k= list(map(int, input().split()))
    # n=int(input())
    # lt= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    # ls=int(input())
    fun(ls)