for _ in range(1):
    var=input()
    st=input()
    # val=int(input())
    # ks= list(map(int, input().split()))
    # ls = list(map(int, input().split()))
    one=st.count('n')
    zero=st.count('z')
    for _ in range(one):
        print('1 ',end=' ')
    for _ in range(zero):
        print('0 ',end=' ')
    print()