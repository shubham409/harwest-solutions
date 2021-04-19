def fun(ls):
    n,k=ls
    v=(2**k)-1
    mod=(10**9)+7
    print(n**k%mod)
    

    
T= int(input())
for i in range(T):
    ls=list(map(int,input().split()))
    fun(ls)