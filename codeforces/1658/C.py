def fun(ls,n):

    count1 =0
    j=0
    for i in ls:
        if i==1:
            count1+=1
            index = j 
        j+=1

    # more than one 1 are not possible only one bigges number is present 
    if(count1!=1 ):
        print('No')
        return

    # rotate about 1 s index 

    # traverse from 1th index to n , 0 to 1th index 
    prv = None
    for i in range (index , n):
        if prv ==None:
            prv = ls[i]
        else:
            if(ls[i]-prv<=1):
                pass
            else:
                print("No")
                return
            prv = ls[i]

    for i in range(0 ,index):
        if prv ==None:
            prv = ls[i]
        else:
            if(ls[i]-prv <= 1):
                pass
            else:
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