from math import ceil
def fun(ls):
    n,m,v=ls
    row = (v%n)
    if row==0:
        row=n
    column = ceil(v/n)
    print(((row-1)*(m))+column)
 
 
 
 
 
T = int(input())
for i in range(T):
    # var=input()
    # st=input()
    # val=int(input())
    # ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls)
    