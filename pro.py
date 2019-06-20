no=input()
a=1
for i in range(len(no)-1):
    ss=no[i]+no[i+1]
    p=int(ss)
    if p<=26 and no[i]!="0":
       a+=1
if a==3:
    print(a)
else:
    print(a+(a-1)//2)
