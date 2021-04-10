def printls(ls):
    for i in ls :
        print(''.join(i))
def fun(ls,n):
    star1=None
    star2=None
    for row ,row_value in enumerate(ls):
        for coulmn,column_value in enumerate(row_value):
            if ( star1 and  star2):
                break
            if(column_value=='*' and star1==None):
                star1=[row,coulmn]
                continue
            if(column_value=='*' and star2==None):
                star2=[row,coulmn]
    row1,coulmn1=star1
    row2,coulmn2=star2
    if(row1==row2 and coulmn1!=coulmn2):
        if( row1!=n-1):
                ls[row1+1][coulmn1]='*'
                ls[row1+1][coulmn2]='*'
        else:
                ls[row1-1][coulmn1]='*'
                ls[row1-1][coulmn2]='*'
        printls(ls)
        return
    if(coulmn1==coulmn2 and row1!=row2):
        if(coulmn1!=n-1 ):
                ls[row1][coulmn1+1]='*'
                ls[row2][coulmn1+1]='*'
        else:
                ls[row1][coulmn1-1]='*'
                ls[row2][coulmn1-1]='*'
        printls(ls)
        return
    else:
        ls[row1][coulmn1]='*'
        ls[row2][coulmn1]='*'
        ls[row1][coulmn2]='*'
        ls[row2][coulmn2]='*'
        printls(ls)
        return
 
 
T = int(input())
for _ in range(T):
    # var=input()
    # st=input()
    n=int(input())
    # a=input()
    # b=input()
    # val=int(input())
    # ms= list(map(int, input().split()))
    lt=[]
    for i in range(n):
        ls= list(input())
        lt.append(ls)
    # n=int(input())
    # st=input()
    fun(lt,n)