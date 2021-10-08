mod = (10**9) +7
def solve(st,base):
    start=0
    ans=0
    for i in st[::-1]:
        if(i=='1'):
            ans+= (base**start)%mod
        start+=1
    return ans%mod


def fun(ls):
    base , k = ls
    summ =0
    count=-1
    if(k==1):
        print(1)
        return
    while(summ<k):
        count+=1
        summ+= (2**count)
        
    last = 2**count
    if(summ==k):
        last_add = 2**(count)
        current = summ - last_add
        in_bin = k-current - 1
        bn = bin(in_bin)[2:]
        st = '1'+ (count-len(bn))*"0"+bn
        print(solve(st,base))
    else:
        last_add = 2**(count)
        current = summ - last_add
        in_bin = k-current - 1
        bn = bin(in_bin)[2:]
        st = '1'+ (count-len(bn))*"0"+bn
        print(solve(st,base))


T = int(input())
for i in range(T):
    ls = list(map(int, input().split()))
    fun(ls)


