s1,s2=input().split()
a=abs(len(s1)-len(s2))
for i in range(len(s1)):
    if len(s2)==1 and s2[i] in s1:
        break
    if s1[i]!=s2[i]:
        a+=1
print(a)
