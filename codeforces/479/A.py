def fun(a,b,c):
    # ls=[a,b,c]
    # ls=sorted(ls)
    # a,b,c=ls
    # print(max(max((a+b),a*b)+c,max((a+b),a*b)*c))
    v= max((a+b+c),((a*b)+c),(a*(b+c)),(a*b*c),(a+(b*c)),((a+b)*c))
    print(v)



# T = int(input())
for i in range(1):
    # var=input()
    # st=input()
    a=int(input())
    b=int(input())
    c=int(input())
    # val=int(input())
    # ms= list(map(int, input().split()))
    # ls= list(map(int, input().split()))
    fun(a,b,c)