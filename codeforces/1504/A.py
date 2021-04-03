def fun(st):
    l=len(st)
    if(st.count('a')==l):
        print('NO')
        return
    else:
        temp=st
        temp=temp+'a'
        if(temp!=temp[::-1]):        
            print('YES')
            print(temp)
            return
        temp=st
        temp='a'+temp
        if(temp!=temp[::-1]):        
            print('YES')
            print(temp)
            return
        else:
            print("NO")
T = int(input())
for i in range(T):
    st=input()
    fun(st)
