def fun(st):
    one=st.count('n')
    zero=st.count('z')
    for i in range(one):
        print('1 ',end=' ')
    for j in range(zero):
        print('0 ',end=' ')
    print()


                             

# T = int(input())
for _ in range(1):
    var=input()
    st=input()
    # val=int(input())
    # ks= list(map(int, input().split()))
    # ls = list(map(int, input().split()))
    fun(st)