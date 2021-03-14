def fun(ls):
    odd= 'I hate'
    even= 'I love'
    mid=' that '
    last=' it'
    ans=''
    for i in range(1,ls+1):
        if i ==1:
            ans+=odd
            continue
        if(i%2==0):
            ans+=(mid+even)
        else:
            ans+=(mid+odd)

    print(ans+last)

# T = int(input())
# for i in range(T):
# n = list(map(int, input().split()))
n = int(input())
# ls = list(map(int, input().split()))
# ipt= input()
fun(n)