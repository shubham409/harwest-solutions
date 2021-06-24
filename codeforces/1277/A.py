for i in range(int(input())):
    a=input()
    b=len(a)
    a=int(a)
    c=int('1'*b)
    d=a//c
    print(d+(9*(b-1)))