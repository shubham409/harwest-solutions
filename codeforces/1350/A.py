def fun(ls):
    n,k=ls
    if(n%2==0):
        print(n+(2*k))
    else:
        odd_divisor=-1
        for i in range(2,n+1):
            if(n%i==0):
                odd_divisor=i
                break
        print(n+odd_divisor+(k-1)*2)

T = int(input())
for i in range(T):
    # var=input()
    # val=int(input())
    # st=input()
    # ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    # ls= list(input())
    # qs=list(map(int, input().split()))
    fun(ls)