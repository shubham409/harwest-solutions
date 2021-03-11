from math import ceil,floor
yes='yes'
no='no'
def fun(st,ls):
    n,k=ls
    # k=k+1
    if(k==0):
        print(yes)
        return
    if(ceil(n/2)<k+1):
        print(no)
        return
    count=0
    for i,val in enumerate(st[:floor(n/2)]):
        from_last=n-1-i
        val_last=st[from_last]
        # print(val,val_last)
        if(val==val_last):
            count+=1
        else:
            if(count<k):
                print(no)
                return
    print(yes)






    
    


    

T = int(input())
for i in range(T):
    # var=input()
    # st=input()
    # val=int(input())
    # ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    st=input()
    fun(st,ls)
    
