from collections import Counter
from math import ceil ,floor
def fun(st):
    dct= Counter(st)
    count1=0
    count0=0
    if('z' in dct):
        if('n' in dct):
            count1=dct.get('n')
            count0=dct.get('z')
        else:
            count0=dct.get('z')

    else:
        count1=dct.get('n')
    print(*(count1*[1]+[0]*count0))


                             

# T = int(input())
for _ in range(1):
    var=input()
    st=input()
    # val=int(input())
    # ks= list(map(int, input().split()))
    # ls = list(map(int, input().split()))
    fun(st)