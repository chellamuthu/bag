from itertools import combinations
string1,num1=map(int,input().split())
n1=len(str(string1))
a1=list(combinations(str(string1),n1-num1))
a1=(sorted(a1))
a2="".join(a1[0])
print(a2)
