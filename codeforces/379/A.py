def fun(ls):
    a,b=ls
    ans=a
    rem=0
    while a+rem>=b:
        a=a+rem
        rem=(a%b)
        a=(a//b)
        ans+=a
    print(ans)



ls= list(map(int, input().split()))
fun(ls)