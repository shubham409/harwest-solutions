from collections import Counter
from math import floor,gcd,ceil
def fun(n):
    st=bin(n)[2:]
    print(Counter(st).get('1'))
fun(int(input()))