import numpy as np

def dotprodukt(a,b):
  if len(a)!=len(b):
    print("Vektorer ikke lige lange")
  else:
    dp=sum([a[i]*b[i] for i in range(len(a))])

  return dp

def transpose(m):
  mud=[[line[col] for line in m] for col in range(len(m[0]))]
  return mud

def matrixmult(m1,m2):
  m3=[] #gemmer resultat
  for col in range(len(m2)):
    mcol=[] #gemmer produkt per kolonne
    collist=[line[col] for line in m2]
    for line in m1:
      mcol.append(dotprodukt(line,collist))
    m3.append(mcol)
  m3=transpose(m3)
  
  return m3

a=[1,2,3]
b=[-4,2,1]

m1=[[1,3,5],[-2,3,1],[4,-3,-1],[-3,6,2]]
#m2=[[1,2,3]]
m2=[[1,2,3],[-3,-2,-1],[2,5,4]]


print(dotprodukt(a,b))

M1=np.array(m1)
M2=np.array(m2)
print(matrixmult(m1,m2))
print("Tjek:")
print(np.matmul(M1,M2))





