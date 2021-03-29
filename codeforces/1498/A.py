from math import gcd
def fun(n):
    grcd=0
    while(grcd<=1):
        sm=sum(list(map(int,list(str(n)))))
        grcd=gcd(n,sm)
        n+=1
    print(n-1)

T = int(input())
for i in range(T):
    st=input()
    fun(int(st))