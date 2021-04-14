var=input()
st=input()
one=st.count('n')
zero=st.count('z')
for _ in range(one):
    print('1 ',end=' ')
for _ in range(zero):
    print('0 ',end=' ')
print()