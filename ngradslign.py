def y(f,x):
  p=len(f)
  yc=sum([f[i]*x**i for i in range(p)])
  return yc

def dy(f,x):
  dx=0.001
  x1=x+dx
  dydx=(y(f,x)-y(f,x1))/(x-x1)
  return dydx

def xny(x0,y0,dy):
  x1=x0-y0/dy
  return x1

def findrod(f,x0):
  while abs(y(f,x0))>0.0001: 
    a=dy(f,x0)
    x0=xny(x0,y(f,x0),a)
  return x0

def sign(tal):
  if tal>=0: 
    s=True
  else:
    s=False
  return s

def findvende(f,xstart):
  dx=0.01
  a0=dy(f,xstart)
  xud=xstart+dx
  a1=dy(f,xud)
  c=0
  while sign(a0)==sign(a1) and c<100:
    c+=1
    xud+=dx
    a1=dy(f,xud)
  if c>=100: print("CMAX")
  return xud

def findnewguess(f,x0,nroot):
  #print(nroot,len(f)-1)
  if nroot<len(f)-2:
    v1=findvende(f,x0)
    v2=findvende(f,v1)
    nytguess=(v1+v2)/2
  else:
    nytguess=findvende(f,x0)
  return nytguess


def findroots(f):
  maxroots=len(f)-1
  nroot=0
  guess=-100
  while nroot<maxroots:
    nroot+=1
    r=findrod(f,guess)
    print("rod",nroot,'{:6.2f}'.format(r))
    if nroot!=maxroots: guess=findnewguess(f,r,nroot)

#f=[-12,2,2]
#f=[6,-7,0,1]
#f=[-12,4,15,-5,-3,1]
#f=[5,3,0,4,-2]
f=[0.25,0,-1.25,0,1]

findroots(f)



