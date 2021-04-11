from math import ceil
import sys 
# sys.setrecursionlimit()

def fun(ls):
    n,k=ls
    st=[i for i in range(1,n+1)]
    rst = st[::-1]
    count=k
    ans=[]
    has=set()
    s=0
    r=0
    i=0
    if(k==0):
        print(*st)
        return
    if((ceil(n/2))-1 <k):
        print(-1)
        return
    while(count !=0):
        if(i%2==0):
            val=st[s]
            has.add(val)
            ans.append(val)
            s+=1
        else:
            val=rst[r]
            has.add(val)
            ans.append(val)
            count-=1
            r+=1
        i+=1
    if s!=n-1:
        while(s<n):
            val=st[s]
            if(val not in has):
                ans.append(val)
                has.add(val)
            s+=1
    print(*ans)


    







    
T = int(input())
# T = 1
for i in range(T):
    # var=input()
    # val=int(input())
    # st=input()
    # ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls)