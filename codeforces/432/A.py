n,k=map(int,input().split()) 
l=[int(x)<=(5-k) for x in input().split()]
print(sum(l)//3) 