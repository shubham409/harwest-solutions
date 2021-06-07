import string
from itertools import product

def fun(ls,n):
    al= string.ascii_lowercase
    ss=list(al)
    for i in range(1,4):
        st=set()
        for j in range(n-i+1):
            st.add(ls[j:j+i])
        al=product( ss ,repeat=i)
        al=(''.join(z) for z in al)
        for k in range(26**i):
            k=next(al)
            if(k not in st):
                print(k)
                return

T = int(input())
for i in range(T):
    n=int(input())
    ls=input()
    fun(ls,n)
    
# Dont use list as it may give MLE use generators or tuple by default give generator