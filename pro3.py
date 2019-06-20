#chella
import sys, string, math

a = int(input())
b = [ int(x) for x in input().split()]
c = 0
for i in range(0,n-2) :
	for j in range(i+1, a-1):
		for k in range(j+1, a ):
			if b[i] < b[j] < b[k] :
				c += 1
				#print(b[i],b[j],b[k],c)

print(c)
