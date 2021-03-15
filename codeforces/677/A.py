def fun(ls,n):
    w=0
    for i in ls:
        if(i>h):
            w+=2
        else:
            w+=1
    print(w)
    
# T = int(input())
for i in range(1):
    # var=input()
    # st=input()
    # val=int(input())
    n,h= list(map(int, input().split()))
    ls = list(map(int, input().split()))
    fun(ls,h)