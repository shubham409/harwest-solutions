def fun(st,n):
    ans1=''
    ans2=''
    count1=st.count('1')
    if(count1%2!=0 or st[-1]!='1' or st[0]!='1'):
        print('No')
        return
    count=0
    alternate=0
    for i in st:
        if(i=='1'):
            count+=1
            if(count<=(count1//2)):
                ans1+='('
                ans2+='('
            else:
                ans1+=')'
                ans2+=')'
        else:
            if(alternate%2==0):
                ans1+='('
                ans2+=')'
            else:
                ans1+=')'
                ans2+='('                
            alternate+=1
    print('Yes')
    print(ans1)
    print(ans2)

T = int(input())
for _ in range(T):
    n=int(input())
    st=input()
    fun(st,n)