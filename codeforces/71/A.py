def fun(x):
    l = len(x)
    if l> 10:
        print(f'{x[0]}{l-2}{x[-1]}')
    else:
        print(x)

T= int(input())
for _ in range(T):
    x= input()
    fun(x)