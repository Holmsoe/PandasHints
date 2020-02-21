import numpy as np

def beregnnyliste(mlist,tal):
  nylist=[]
  for line in mlist:
    for j in range(len(line)+1):
      temp=[item for item in line]
      temp.insert(j,tal)
      nylist.append(temp)
  return nylist

def permutationer(n):
  listeny=[[0]]
  for i in range(1,n+1):
    listeny=beregnnyliste(listeny,i)
  return listeny

def inversioner(liste):
  count=0
  p=liste
  for i in range(len(p)):
    for j in range(i+1,len(p)):
      if p[j]<p[i]: count+=1
  return count

def mdet(matr):
  permutliste=permutationer(len(matr)-1)
  determ=0
  for pline in permutliste:
    prod=1
    for im in range(len(m)):
      prod*=matr[im][pline[im]]
    if inversioner(pline)%2==0:
      determ+=prod
    else:
      determ-=prod
  return determ


m=[[5,8,6,9],[-7,9,3,5],[-7,-10,-8,2],[-1,8,9,-6]]

print(mdet(m))
print(np.linalg.det(m))


  
    
    
  


    
  



