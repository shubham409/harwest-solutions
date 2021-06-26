t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a=[0]+a+[0]
    ans=0
    for i in range(1,n+1):
        if(a[i]>a[i-1] and a[i]>a[i+1]):
            ans+=a[i]-max(a[i-1],a[i+1])
            a[i]=max(a[i-1],a[i+1])
    for i in range(1,n+1):
        ans+=max(0,a[i]-a[i-1])+max(0,a[i]-a[i+1])
    print(ans)