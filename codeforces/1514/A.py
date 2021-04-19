from math import floor, gcd,ceil,sqrt
def checksquare(n):
    s=sqrt(n)
    a=ceil(s)
    b=floor(s)
    if ((a*a)==n and n==b*b):
        return True
    else:
        return False
def fun(ls,n):
    count_non_square=0
    for i in ls:
        var=checksquare(i)
        if(var==False):
            count_non_square+=1
    if(count_non_square>0):
        print('Yes')
    else:
        print('No')
    

T = int(input())
for i in range(T):
    val=int(input())
    ls= list(map(int, input().split()))    
    fun(ls,val)