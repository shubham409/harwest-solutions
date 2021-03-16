def fun(st):
    if(st.isupper()):
        print(st.lower())
        return
    if(st[1::].isupper()):
        print(st.capitalize())
        return
    if(len(st)==1 and st.lower()):
        print(st.upper())
    else:
        print(st)


# T = int(input())
for i in range(1):
    # var=input()
    st=input()
    # val=int(input())
    # ms= list(map(int, input().split()))
    # ls= list(map(int, input().split()))
    fun(st)
    



