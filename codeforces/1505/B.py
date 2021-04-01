inpt=input()
ans=sum(list(map(int,list(inpt))))
while (ans>9):
    inpt=str(ans)
    ans=sum(list(map(int,list(inpt))))
print(ans)