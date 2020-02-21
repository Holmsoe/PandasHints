import time 
import numpy as np

class lavenhedsmatrix():
  def __init__(self,m):
    self.tolerance=1e-10
    self.mgem=m
    self.n=len(self.mgem)

#Styring af beregningsmatrix
#===========================
  def beregn(self,rs):
    self.rs=[[i for i in line] for line in rs]
    self.rsgem=rs
    #nulstil beregningsmatrix
    self.m=[[i for i in line] for line in self.mgem]
    self.NulUnderDiagonal()
    self.EnhedsMatrix()
#===========================

#Standard rækkeoperation på matrix:matr,faktor der anvendes,pivotlinie,korrigeret line
#============================
  def rowoperate(self,matr,fak,piv,lin):
    for nr,item in enumerate(matr[lin]):
      matr[lin][nr]=item-fak*matr[piv][nr]
    return matr
#=============================

#Ved rækkeoperationer fås nuller under diagonalen
#===========================

  def NulUnderDiagonal(self):
    self.rowtaken=[]
    for col in range(self.n):
      self.NullifyCol(col)
    self.sortermatrix()
    

  def NullifyCol(self,col):
    pivotline=self.MaxAbsCol(col)
    for line in range(self.n):
      if line not in self.rowtaken:
        fak=self.m[line][col]/self.m[pivotline][col]
        self.m=self.rowoperate(self.m,fak,pivotline,line)
        self.rs=self.rowoperate(self.rs,fak,pivotline,line)

  def MaxAbsCol(self,col):
    abskolonne=[abs(line[col]) if nr not in self.rowtaken else 0 for nr,line in enumerate(self.m)]
    linienr=[i for i,item in enumerate(abskolonne) if max(abskolonne)==item][0]
    self.rowtaken.append(linienr)
    return linienr

#Slut på nuller under diagonalen
#==============================


#På basis af matrix med nuller under diagonalen beregnes enhedsmatrix
#==================================
  def EnhedsMatrix(self):
    w=self.n
    for i in reversed(range(self.n)):
      for j in range(i):
        fak=self.m[j][i-w]/self.m[i][i-w]
        self.m=self.rowoperate(self.m,fak,i,j)
        self.rs=self.rowoperate(self.rs,fak,i,j) 
    for i in range(self.n):
      #rs kan have forskellig bredde. Kan være en søjle eller en matrix så vi må rette hvert element
      for nr,item in enumerate(self.rs[i]):
        self.rs[i][nr]=self.rs[i][nr]/self.m[i][i]
      self.m[i][i]=self.m[i][i]/self.m[i][i]
    
  def sortermatrix(self):
    sortmatrix=[]
    rssort=[]
    for i in range(self.n):
      sortmatrix.append(self.m[self.findlinie(i)])
      rssort.append(self.rs[self.findlinie(i)])
    self.m=sortmatrix
    self.rs=rssort

  def findlinie(self,n):
    for row in range(self.n):
      if abs(sum(self.m[row])-sum(self.m[row][n:self.n]))<self.tolerance and abs(self.m[row][n])>self.tolerance :
        linieregn=row 
    return linieregn

#Slut på enhedsmatrix
#========================

class matrixinvert(lavenhedsmatrix):
  def __init__(self,m):
    lavenhedsmatrix.__init__(self,m)

  def finninvert(self):
    enhedsm=[[1 if i==j else 0 for i in range(4)] for j in range(4)]
    self.beregn(enhedsm)
    return self.rs

class matrixsolve(lavenhedsmatrix):
  def __init__(self,m):
    lavenhedsmatrix.__init__(self,m)

  def finnsolve(self,rs):
    if len(rs[0])!=1: 
      print("Input skal være søjlematrix")
    else:
      self.beregn(rs)
    return self.rs


#Start på klasse tilberegning af determinant
#==========================================
class matrixdeterm():
  def __init__(self,m):
    self.m=m

  #Beregning af determinant
  def mdet(self):
    matr=self.m
    permutliste=self.permutationer(len(matr)-1)
    determ=0
    for pline in permutliste:
      prod=1
      for im in range(len(m)):
        prod*=matr[im][pline[im]]
      if self.inversioner(pline)%2==0:
        determ+=prod
      else:
        determ-=prod
    return determ

  #Beregning af alle permutationer fra 0 til n-1
  def permutationer(self,n):
    listeny=[[0]]
    for i in range(1,n+1):
      listeny=self.beregnnyliste(listeny,i)
    return listeny

  def beregnnyliste(self,mlist,tal):
    nylist=[]
    for line in mlist:
      for j in range(len(line)+1):
        temp=[item for item in line]
        temp.insert(j,tal)
        nylist.append(temp)
    return nylist
  #Slut på permutationer

  #Beregning af antal inversioner for en permutation
  def inversioner(self,liste):
    count=0
    p=liste
    for i in range(len(p)):
      for j in range(i+1,len(p)):
        if p[j]<p[i]: count+=1
    return count
  #Slut på beregning af inversioner


#Start på klasse til multiplikation af matricer
#==========================================

class matrixmult():
  def __init__(self,m1,m2):
    self.m1=m1
    self.m2=m2

  def matmult(self):
    m1=self.m1
    m2=self.m2
    m3=[] #gemmer resultat
    for col in range(len(m2)):
      mcol=[] #gemmer produkt per kolonne
      collist=[line[col] for line in m2]
      for line in m1:
        mcol.append(self.dotprodukt(line,collist))
      m3.append(mcol)
    m3=self.transpose(m3)  
    return m3

  def dotprodukt(self,a,b):
    if len(a)!=len(b):
      print("Vektorer ikke lige lange")
    else:
      dp=sum([a[i]*b[i] for i in range(len(a))])
    return dp

  def transpose(self,m):
    mud=[[line[col] for line in m] for col in range(len(m[0]))]
    return mud

#Slut på klasse til multiplikation af matricer
#==========================================

class matmultk():
  def __init__(self,k,m):
    self.k=k
    self.m=m
    self.d=len(self.m)

  def mmultk(self):
    mud=[[self.m[i][j]*self.k for i in range(self.d)] for j in range(self.d)]
    return mud

#Opløfte matrix til n'te potens 
class matpow():
  def __init__(self,m,n):
    self.m=m
    self.mny=m
    self.n=n
    
  def mpow(self):
    for i in range(self.n):
      self.mny=matrixmult(self.m,self.mny).matmult()
    return self.mny

#Beregne trace af matrix (sum af diagonal 
class mattrace():
  def __init__(self,m):
    self.m=m
    self.d=len(m)

  def tr(self):
    tr=[[self.m[i][j] if i==j else 0 for i in range(self.d)] for j in range(self.d)]
    trsum=sum([sum(line) for line in tr])
    return trsum

class karaklign():
  '''
  Finde koefficienter til karakteristisk polynomium
  https://en.wikipedia.org/wiki/Faddeev%E2%80%93LeVerrier_algorithm
  '''
  def __init__(self,m):
    self.m=m 

  def lign(self):
    n=len(self.m)
    c=[0 for tal in range(n+1)]
    E=[[1 if i==j else 0 for i in range(n)] for j in range(n)]
    c[n]=1
    M=[[0 for i in range(n)] for j in range(n)]
    A=self.m
    for k in range(1,n+1):
      AM=matrixmult(A,M).matmult()
      cI=matmultk(c[n-k+1],E).mmultk()
      M=[[(AM[i][j]+cI[i][j]) for j in range(n)] for i in range(n)]
      AM=matrixmult(A,M).matmult()
      c[n-k]=-mattrace(AM).tr()/k
    #c.reverse()
    return c

class quadeq():
  def __init__(self,koeff):
    self.koef=koeff

  def findroots(self):
    f=self.koef
    maxroots=len(f)-1
    nroot=0
    guess=-100
    while nroot<maxroots:
      nroot+=1
      r=self.findrod(f,guess)
      print("rod",nroot,'{:6.2f}'.format(r))
      if nroot!=maxroots: guess=self.findnewguess(f,r,nroot)

  def findrod(self,f,x0):
    while abs(self.y(f,x0))>0.0001: 
      a=self.dy(f,x0)
      x0=self.xny(x0,self.y(f,x0),a)
    return x0

  def findnewguess(self,f,x0,nroot):
    #print(nroot,len(f)-1)
    if nroot<len(f)-2:
      v1=self.findvende(f,x0)
      v2=self.findvende(f,v1)
      nytguess=(v1+v2)/2
    else:
      nytguess=self.findvende(f,x0)
    return nytguess

  def findvende(self,f,xstart):
    dx=0.01
    a0=self.dy(f,xstart)
    xud=xstart+dx
    a1=self.dy(f,xud)
    c=0
    while self.sign(a0)==self.sign(a1) and c<100:
      c+=1
      xud+=dx
      a1=self.dy(f,xud)
    if c>=100: print("CMAX")
    return xud

  def y(self,f,x):
    p=len(f)
    yc=sum([f[i]*x**i for i in range(p)])
    return yc

  def dy(self,f,x):
    dx=0.001
    x1=x+dx
    dydx=(self.y(f,x)-self.y(f,x1))/(x-x1)
    return dydx

  def xny(self,x0,y0,dy):
    x1=x0-y0/dy
    return x1

  def sign(self,tal):
    if tal>=0: 
      s=True
    else:
      s=False
    return s

#Her er hovedprogram
#===================
def printm(mprint):
  for line in mprint:
    for item in line:
      print('{:8.2f}'.format(item),end="")
    print("")

#m1=[[5,8,6,9],[-7,9,3,5],[-7,-10,-8,2],[-1,8,9,-6]]
#rs=[[-100],[-150],[29],[-49]]
m=[[7,2,4,-3],[0,6,5,9],[0,6,2,5],[-8,-1,-7,-8]]
#E4=[[1 if i==j else 0 for i in range(4)] for j in range(4)]
#E3=[[1 if i==j else 0 for i in range(3)] for j in range(3)]
#print(E4)
rs=[[-73],[67],[59],[45]]
rs1=[[1 if i==j else 0 for i in range(4)] for j in range(4)]
mtest=[[3,1,5],[3,3,1],[4,6,4]]

print("")
print("Løs ligninger")
printm(matrixsolve(m).finnsolve(rs))
A=np.array(m)
b=np.array(rs)
print("")
print("Tjek løs ligninger")
printm(np.linalg.solve(A,b))
print("")
print("Beregn invers")
printm(matrixinvert(m).finninvert())
print("")
print("Tjek invers matrix")
printm(np.linalg.inv(A))
print("")
print("Determinant     ",matrixdeterm(m).mdet())
print("Tjek determinant",'{:8.4f}'.format(np.linalg.det(m)))
print("")
printm(matrixmult(m,m).matmult())
print("Tjek multiplikation")
M1=np.array(m)
M2=np.array(m)
print(np.matmul(M1,M2))
print("")
print(karaklign(mtest).lign())
print("Tjek karakterlign")
Mtest=np.array(mtest)
print(np.poly(Mtest))
print(np.poly(Mtest)[::-1]) #reverse numpy array

c=karaklign(mtest).lign()
print(c)
quadeq(c).findroots()
c.reverse()
ctest=np.array(c) 
print(np.roots(ctest))

