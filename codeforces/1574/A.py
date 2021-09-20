def fun(n):
    s=''
    for i in range(n):
        s='('+s+')'
    now=''
    for i in range(n):
        if i==0:
            print(s)
        else:
            now+= '('+')'
            s= s[1:-1]
            print(now+s)
T = int(input())
for i in range(T):
    n = int(input())
    fun(n)