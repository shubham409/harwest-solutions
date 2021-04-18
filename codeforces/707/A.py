def fun(st):
    c='C' 
    m='M' 
    y='Y' 

    w='W' 
    g='G' 
    b='B'
    if(c in st or m in st or y in st) :
        print('#Color')
    else:
        print('#Black&White')
    


                             

# T = int(input())
T,n = list(map(int, input().split()))
st=set()
for _ in range(T):
    # var=input()
    # st=input()
    # val=int(input())
    # ks= list(map(int, input().split()))
    ls = list( input())
    st=st.union(ls)
fun(st)