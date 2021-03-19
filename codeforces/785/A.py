def fun(ls):
    ans=0
    dct={'Tetrahedron' :4,
    'Cube' :6,
    'Octahedron' :8,
    'Dodecahedron' :12,
    'Icosahedron' :20}
    for i in ls:
        ans+=dct.get(i)
    print(ans)



T = int(input())
ls=[]
for i in range(T):
    # var=input()
    # st=input()
    # val=int(input())
    st=input()
    # lt= list(map(int, input().split()))    
    # ls= list(map(int, input().split()))    
    ls.append(st)
    # fun(val,ls,lt)
fun(ls)