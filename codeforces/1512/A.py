from collections import Counter
from math import ceil

def fun(ls,n):
    dct=Counter(ls)
    key=dct.keys()
    for i in key:
        if dct.get(i)==1:
            print(ls.index(i)+1)
            return

            


    
T = int(input())
for _ in range(T):
    # var=input()
    # st=input()
    n=int(input())
    # a=input()
    # b=input()
    # val=int(input())
    # ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    # n=int(input())
    # st=input()
    fun(ls,n)