from collections import Counter
def fun(ls,lt,n):
    zero_zero=0
    one_one=0
    mex=0
    for i in range(n):
        ls_val= ls[i]
        lt_val= lt[i]
        if(ls_val!=lt_val):
            mex+=2+zero_zero
            zero_zero=0
            one_one=0
            continue

        if(i==0):
            if(ls_val == 0 and ls_val == 0):
                if one_one == 0:
                    zero_zero+= 1
                else:
                    mex+=2
                    one_one=0
                    zero_zero=0
            else:
                if zero_zero == 0:
                    one_one+=1
                else:
                    one_one=0
                    zero_zero-=1
                    mex+=2
                    if zero_zero>=1 :
                        mex+=zero_zero
                    zero_zero=0

        else:
            if(ls_val == 0 and ls_val == 0):
                if one_one == 0:
                    zero_zero+= 1
                else:
                    mex+=2
                    one_one=0
                    zero_zero=0
            else:
                if zero_zero == 0:
                    one_one+=1
                else:
                    one_one=0
                    zero_zero-=1
                    mex+=2
                    if zero_zero>=1 :
                        mex+=zero_zero
                    zero_zero=0
    
    if zero_zero>=1:
        mex+=zero_zero

    print(mex)

T = int(input())
for i in range(T):
    n = int(input())
    st= input()
    ls = list(map(int, list(st)))
    st= input()
    lt = list(map(int, list(st)))
    fun(ls,lt,n)
