def fun(st):
    if(''.join(sorted(st)) == st):
        print('YES')
        return
    start =st.find('11')
    stop=st.find('00',start)
    if(start!=-1 and stop!=-1):
        print('NO')
        return
    print('YES')
    
T = int(input())
for i in range(T):
    st=input()
    fun(st)