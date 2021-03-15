def fun(ls,n):
    j=1
    dct={}
    for i in ls:
        dct[i]=j
        j+=1
    for i in range(1,n+1):
        print(dct.get(i),end=' ')
    print()

    
# T = int(input())
for i in range(1):
    # var=input()
    # st=input()
    val=int(input())
    # n,h= list(map(int, input().split()))
    ls = list(map(int, input().split()))
    fun(ls,val)
    # fun(st,var)