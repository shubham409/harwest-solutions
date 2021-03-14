from collections import Counter
from math import ceil


def fun(ls,n):
    st = sorted(ls)
    # print(st)
    # if(st[-1] >= st[0] + st[1] + st[2]):
    #     print('No')
    #     return
    dct = {}
    number_of_occurence = Counter(ls)
    for i, val in enumerate(ls):
        if(val in dct):
            dct[val].append(i)
        else:
            dct[val] = [i]
    # if repeating 4 or repeating 2 is present
    two_repeating = []
    for key, lst in dct.items():
        if number_of_occurence[key] >= 4:
            print('YES')
            print(lst[0]+1, lst[1]+1, lst[2]+1, lst[3]+1)
            return
        # print(number_of_occurence)
        if(number_of_occurence[key] >= 2):
            two_repeating.append(key)
            if(len(two_repeating) == 2):
                f = dct.get(two_repeating[0])
                s = dct.get(two_repeating[1])
                print('YES')
                print(f[0]+1, s[0]+1, f[1]+1, s[1]+1)
                return

    duplicates={}#sum : index
    for i in range(n//2, n):
        for j in range(0,i):
            v1=st[i]
            v2=st[j]
            get_index_of_i=None
            get_index_of_j=None
            if(v1!=v2):
                get_index_of_i=dct[v1][0]
                get_index_of_j=dct[v2][0]
            else:
                get_index_of_i=dct[v1][0]
                get_index_of_j=dct[v2][1]
            sm =v1+v2
            if sm not in duplicates:
                duplicates[sm]=[[get_index_of_i,get_index_of_j]]
            else:
                get_sum = duplicates[sm][0]
                if(get_index_of_i+1!=get_sum[0]+1 and get_index_of_j+1!=get_sum[1]+1):
                    print('YES')
                    print(get_index_of_i+1,get_index_of_j+1,get_sum[0]+1,get_sum[1]+1)
                    return
    print('NO')

    


T = int(input())
for i in range(1):
    # var=input()
    # st=input()
    # val=int(input())
    # lt= list(map(int, input().split()))
    ls = list(map(int, input().split()))
    fun(ls,T)
