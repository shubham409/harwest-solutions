from math import ceil
def fun(x):
    l=x[0]
    b= x[1]
    a=x[2]

    n1= ceil(l/a)
    n2= ceil(b/a)
    print(n1*n2)


x= input().split(' ')
x= list (map(int , x))
fun(x)