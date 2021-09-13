from collections import Counter
def fun(ls):
    ctr= dict(Counter(ls))
    count_0=0
    count_1=0
    if ctr.get(0) == None:
        count_0 = 0
    else:
        count_0 = ctr.get(0)
    
    if ctr.get(1) == None:
        count_1 = 0
    else:
        count_1 = ctr.get(1)
    
    count_zero_together=0
    for i in ls:
        if(i==1):
            if(count_zero_together!=0):
                break
        else:
            count_zero_together+=1
    all_zero_together = count_zero_together==count_0
    if(count_0==0):
        print(0)
        return
        # alll one
 
    if(count_0==1):
        print(1)
        return
        # one zero
 
    if(count_1==0):
        print(1)
        return
        # all zero
    if(all_zero_together):
        print(1)
        return
 
    print(2)
    return

T = int(input())
for i in range(T):
    st= input()
    ls = list(map(int, list(st)))
    fun(ls)
 
        