def fun(lt):
    if(min(lt)%2==0):
        print('Malvika')
    else:
        print('Akshat')

for i in range(1):
    ls= list(map(int, input().split()))
    fun(ls)