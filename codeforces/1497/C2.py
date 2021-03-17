from math import ceil ,floor
def privious(ls):
    n,k=ls
    if(n%2!=0):
        a=floor(n/2)
        b=floor(n/2)
        c=1
        print(a,b,c)
    else:
        if((n//2)%2==0):
            a=(n//2)
            b=(n//4)
            c=(n//4)
            print(a,b,c)
        else:
            a=(n//2)-1
            remaining = n-a
            b=a
            c=n-(2*a)
            print(a,b,c)

def fun(ls):
    n,k=ls
    extra=k-3

    for i in range(extra):
        print(1,end=' ')
    privious([n-extra,k-extra])
                             

T = int(input())
for i in range(T):
    # var=input()
    # st=input()
    # val=int(input())
    # n,k= list(map(int, input().split()))
    ls = list(map(int, input().split()))
    fun(ls)