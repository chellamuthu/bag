#chellamuthu
mat,jit=map(str,input().split())
sun=0
if len(mat)>len(jit):
  mat,jit=jit,mat
i=0
while i<len(mat):
  sun+=(ord(jit[i])-ord(mat[i]))
  i+=1
for i in range(i,len(jit)):
  sun+=ord(jit[i])-ord('a')+1
print(sun)
