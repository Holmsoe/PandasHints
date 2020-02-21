import numpy as np
import pandas as pd
import math  
import matplotlib.pyplot as plt

def fac(n):
  return math.factorial(n)

def komb(n,k):
  r=int(fac(n)/fac(k)/fac(n-k))
  return r

def pformel(p,n,s):
  # se http://mathworld.wolfram.com/Dice.html
  psum=0
  kmax=math.floor((p-n)/s)
  for k in range(kmax+1):
    k1=komb(n,k)
    k2=komb(p-s*k-1,n-1)
    psum+=(-1)**k*k1*k2
  return psum

def terning(s):
  return np.random.randint(1,s+1)

def multiterning(n,s):
  tsum=0
  for i in range(1,n+1):
    tsum+=terning(s) 
  return tsum

def spil(n,s,nslag):
  aktueludfald=[0 for i in range(n,n*s+1)]
  for i in range(nslag):
    msum=multiterning(n,s)
    aktueludfald[msum-n]+=1
  return aktueludfald

def pctfunc(x,colsum):
  return x/colsum*100

p=7 # sum
n=3 # antal terninger
s=6 # antal sider
nslag=s**n
#nslag=1000

udfald=[n for n in range(n,n*s+1)]
ptabel=pd.DataFrame()
ptabel['udfald']=udfald
ptabel['pudfald']=ptabel['udfald'].apply(pformel,p,n=n,s=s)

spiludfald=spil(n,s,nslag)
ptabel['spiludfald']=spiludfald
ptabel['pctformel']=ptabel['pudfald'].apply(pctfunc,colsum=ptabel['pudfald'].sum())
ptabel['pctspil']=ptabel['spiludfald'].apply(pctfunc,colsum=ptabel['spiludfald'].sum())

ptabel['pctformel'] = ptabel['pctformel'].apply("{0:.2f}".format)
ptabel['pctspil'] = ptabel['pctspil'].apply("{0:.2f}".format)

print(ptabel)

ptabel[["pctformel"]] = ptabel[["pctformel"]].apply(pd.to_numeric, errors='coerce')
ptabel[["pctspil"]] = ptabel[["pctspil"]].apply(pd.to_numeric, errors='coerce')

plt.bar(ptabel['udfald'],ptabel['pctspil'])
plt.plot(ptabel['udfald'],ptabel['pctformel'],color='red')



