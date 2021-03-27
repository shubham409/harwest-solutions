def fun(n):
    if(n==2 or n==1):
        print(1)
        return
    if(n%2==0):
        print(n//2)
    else:
        print(1+(n//2))


T = int(input())
for i in range(T):
    v=(int(input()))
    fun(v)