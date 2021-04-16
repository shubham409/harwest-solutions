def fun(ls):
    countt=0
    countm=0
    t='T'
    m='M'
    for i in ls:
        if i==m:
            countm+=1
        else:
            countt+=1
    if(countt!=countm*2):
        print('No')
        return
    else:    
        countt=0
        countm=0
        if(ls[0]==m or ls[-1]==m):
            print('No')
            return
        for i in ls:
            if i==t:
                countt+=1
            if i==m:
                countm+=1
            if(countm>countt):
                print('No')
                return
        countt=0
        countm=0
        for i in ls[::-1]:
            if i==t:
                countt+=1
            if i==m:
                countm+=1
            if(countm>countt):
                print('No')
                return
    print('Yes')
T = int(input())
for i in range(T):
    val=int(input())
    ls= list(input())
    fun(ls)