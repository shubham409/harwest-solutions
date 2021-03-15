def fun(ls,n):
    for i in range(n):
        ls=ls.replace('BG','GB')
    print(ls)
    
# T = int(input())
for i in range(1):
    k,n= list(map(int, input().split()))
    st=input()
    # val=int(input())
    # ls = list(map(int, input().split()))
    # fun(ls,T)
    fun(st,n)