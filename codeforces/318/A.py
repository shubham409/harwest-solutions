from math import ceil
def fun(ls):
    n,k=ls
    mid=(ceil (n/2))
    if(k<=mid):
        print((2*k)-1)
    else:
        k=k-mid
        print(2*k)


    
    

# T = int(input())
for i in range(1):
    # var=input()
    # st=input()
    # val=int(input())
    # ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls)