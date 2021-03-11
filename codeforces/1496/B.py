from math import ceil


def fun(ls,ms):
    n,k=ms
    st=set(ls)
    missin_val=0
    max_val=-1
    st=sorted(ls)
    missin_val=0
    max_val=st[-1]
    first_missing=-1
    for i in st:
        if(i==missin_val):
            missin_val+=1
        else:
            if(i>missin_val):
                first_missing=missin_val
                break
    if(first_missing==-1):
        first_missing=max_val+1
    # print(first_missing)
    if(k==0):
        print(n)
        return
    if(first_missing>max_val):
        print(n+k)
        return
    if(ceil((first_missing+max_val)/2) in st):
        print(n)
        return
    if(ceil((first_missing+max_val)/2) != first_missing):
        print(n+1)
        return    


    



    
    

T = int(input())
for i in range(T):
    # var=input()
    # st=input()
    # val=int(input())
    ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls,ms)


