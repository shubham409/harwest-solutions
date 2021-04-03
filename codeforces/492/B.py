def fun(ls,ms):
    ls=sorted(ls)
    max_dis=0
    prv=ls[0]
    for i in ls[1:]:
        max_dis=max(max_dis,abs(prv-i))
        prv=i
    if(max_dis>2*(ls[0]-0) and max_dis>2*(ms[1]-ls[-1])):
        print('%.8f'%(max_dis/2))
    else:
        if(ls[0]>ms[1]-ls[-1]):
            print('%.8f'%(ls[0]))
        else:
            print('%.8f'%(ms[1]-ls[-1]))


for i in range(1):
    ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls,ms)