import time 
import numpy as np

class elim():
  '''
  På basis af ligningssæt og højreside diagonaliseres matrix. 
  Output er den diagonaliserede matrix og den tilhørende højreside. Disse hentes med hhv. equd og rsud.
  For hver kolonne findes største absolutte værdi som anvendes som pivotlinie. (giver mere robust beregning)
  '''
  def __init__(self,eq,rs):
    self.eq=eq
    self.rs=rs
    self.rowtaken=[]
    for col in range(len(self.eq)-1):
      npivot=self.findpivot(col)
      self.rowtaken.append(npivot)
      self.elimcol(npivot,col)
   
  def equd(self):
    return self.eq 

  def rsud(self):
    return self.rs     

  def findpivot(self,col):
    '''
    abskolonne er en liste med absolutte værdier i aktuel kolonne. Hvis kolonnen allerede har været brugt indsættes 0
    Linienr for maximal absolut værdi i kolonnen. Der genereres en liste. Derfor vælges første element med [0]
    '''
    abskolonne=[abs(line[col]) if nr not in self.rowtaken else 0 for nr,line in enumerate(self.eq)]
    linienr=[i for i,item in enumerate(abskolonne) if max(abskolonne)==item][0]
    return linienr
    
  def elimcol(self,npivot,col):
    '''
    Eliminere alle i kolonne=col på basis af linien npivot
    For hver linie beregnes faktor og npivotrækken ganges med faktor og fratrækkes aktuel række. Også højresiden medregnes.
    '''   
    for row in range(len(self.eq)):
      if row not in self.rowtaken:
        faktor=self.eq[row][col]/self.eq[npivot][col]
        for j in range(len(self.eq)): 
          self.eq[row][j]-=self.eq[npivot][j]*faktor
        self.rs[row]-=self.rs[npivot]*faktor

class calcvar():
  def __init__(self,eqelim,rselim):
    self.tolerance=1e-10
    self.eq=eqelim
    self.rs=rselim
    self.x=[0 for i in range(len(self.eq))]
    self.beregnvar()

  def xud(self):
    return self.x

  def beregnvar(self):
    '''
    Vi tæller baglæns og finder xn fra toppen fra den eliminerede ligning.
    xi er variabelnummeret
    Vi anvender de større x værdier til at finde (xi+1)*fak(xi+1)+(xi+1)*fak(xi+1)
    Denne sum fratrækkes højresiden
    Eks. vi arbejdet på x2 og har linien 0 f2 f3 f4 =h1
    Her bliver x2=(h1-(x3*f3+x4*f4))/f2
    For højeste x er der ikke noget at trække fra
    '''
    for xi in reversed(range(len(self.eq))):
      xnr=xi      
      linenr=self.findlinie(xnr)
      sumrest=0
      if xnr<len(self.eq)-1: 
        for j in range(xnr+1,len(self.eq)):
          sumrest+=self.x[j]*self.eq[linenr][j]
      self.x[xnr]=(self.rs[linenr]-sumrest)/self.eq[linenr][xnr]
      
  def findlinie(self,n):
    '''
    #findlinie finder den linie som har xi som første variabel. eks hvis vi har 4 variable og ønsker at finde linie med x3 som første, leder vi efter formen 0 0 5 6
    Kriterie for linie er, at sum af leddene fra x3 = totalsum
    '''
    nvar=len(self.eq)
    for row in range(nvar):
      if abs(sum(self.eq[row])-sum(self.eq[row][n:nvar]))<self.tolerance and abs(self.eq[row][n])>self.tolerance :
        linieregn=row 
    return linieregn

start = time.time()
#equations=[[5,8,6,9],[-7,9,3,5],[-7,-10,-8,2],[-1,8,9,-6]]
#rightside=[-100,-150,29,-49]
equations=[[7,2,4,-3],[0,6,5,9],[0,6,2,5],[-8,-1,-7,-8]]
rightside=[-73,67,59,45]

minligning=elim(equations,rightside)
eqelim=minligning.equd()
rselim=minligning.rsud()
'''
for line in eqelim:
  print('{:6.2f}{:6.2f}{:6.2f}{:6.2f}'.format(*line))
print(rselim)
'''
minligning1=calcvar(eqelim,rselim)
end = time.time()
for item in minligning1.xud():
  print('{:6.2f}'.format(item),end="")
end = time.time()
print("")
print('{:6.2f}'.format(1e6*(end - start)),"millisekunder")

start = time.time()
A=np.array(equations)
b=np.array(rightside)
x=np.linalg.solve(A,b)
end = time.time()
print('{:6.2f}'.format(1e6*(end - start)),"millisekunder")


print("")
print("Tjek:")
print(x)

'''
print(elim.__doc__)
print(elim.findpivot.__doc__)
print(elim.elimcol.__doc__)
'''




