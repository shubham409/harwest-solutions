n,x=map(int,input().split())
print(sum((x%i==0and x/i<=n)for i in range(1,n+1)))