def fun(ls,k):
    repeating=[]
    unique=[]
    st=set()
    for i in ls:
        if(i not in st):
            st.add(i)
            unique.append(i)
        else:
            repeating.append(i)
    print(*(sorted(unique)+sorted(repeating)[::--1]))

T = int(input())
for i in range(T):
    v=int(input())
    ls= list(map(int, input().split()))
    fun(ls,v)