def fun(ls):
    hr,mn=ls
    hr=23-hr
    mn=60-mn
    print(hr*60+mn)
    
T = int(input())
for i in range(T):
    ls= list(map(int, input().split()))
    fun(ls)