def fun(ls,n):
    prv=None

    count1 =0
    j=0
    for i in ls:
        if prv ==None:
            prv = i

        else:
            if(i-prv>1):
                print("No")
                return
            prv = i 

        if i==1:
            count1+=1
            index = j 
        j+=1

    if(count1!=1 ):
        print('No')
        return

    # rotate about j 
    prv = None
    for i in range (index , n):
        if prv ==None:
            prv = ls[i]
        else:
            if(ls[i]-prv>1):
                print("No")
                return
            prv = ls[i]

    for i in range(0 ,index):
        if prv ==None:
            prv = ls[i]
        else:
            if(ls[i]-prv>1):
                print("No")
                return
            prv = ls[i]    
    print('Yes')



T = int(input())
for i in range(T):
    # st=input()
    n=int(input())
    ls= list(map(int, input().split()))
    # lt= list(map(int, input().split()))
    fun(ls,n)
