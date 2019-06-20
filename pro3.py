# chella
a=int(input())

b=list(map(int,input().split()))

e=0

for i in range(len(b)-2):

    for x in range(i+1,len(b)-1):

         for j in range(x+1,len(b)):

            if b[i]<b[x]<b[j] and i<x<j:

                e+=1

print(e)    
