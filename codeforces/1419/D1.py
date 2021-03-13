def fun(ls,n):
    if(n==1 or n==2):
        print(0)
        print(*ls)
        return
    position= n//2
    index= position-1
    ls=sorted(ls)
    ans=[0 for i in range(n)]
    even=n-1
    odd=0
    for i in range(n):
        if(i%2==0):
            ans[i]=ls[even]
            even-=1
        else:
            ans[i]=ls[odd]
            odd+=1
    if(n%2!=0):
        print(n//2)
    else:
        print((n//2)-1)
    print(*ans)

    

        

# T = int(input())
# for i in range(T):
# n = list(map(int, input().split()))
n = int(input())
ls = list(map(int, input().split()))
fun(ls,n)