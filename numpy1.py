

import numpy as np 
import random as rd 

class npbasic():
  def __init__(self,a,b,p):
    self.a=a
    self.b=b
    self.p=p
    self.eksempler()

  def eksempler(self):
    a1=self.a 
    b1=self.b
    p1=self.p
    c1=np.arange(1,4)
    print("sum")
    print(np.add(a1,b1))
    print(a1+b1)
    print("Broadcasting. Det mindste array gentages")
    print("lille array",c1)
    print(a1+c1)
    print("læg tal til")
    print(np.add(a1,7))
    print(a1+np.full((3,3),7))
    print("diff")
    print(np.subtract(a1,b1))
    print(a1-b1)
    print("gange med tal")
    print(np.multiply(a1,3))
    print(a1*np.full((3,3),3)) 
    print("gange array elementvis")
    print(np.multiply(a1,b1))
    print(a1*b1)
    print("produkt af matricer")
    print(np.matmul(a1,b1))
    print("Divider elementvis")
    print(np.divide(a1,b1))
    print(a1/b1)
    print("opløft til potens")
    print(np.power(a1,2))
    print(a1**2)
    print("opløft til potens fra matrix")
    print(p1)
    print(np.power(a1,p1))
    print("antal elementer - to måder",np.size(a1),a1.size)
    print("dimensioner - to måder",np.shape(a1),a1.shape)
    print("type", a1.dtype)
    print("konverter til liste")
    print(a1.tolist())

    print("iteration med nditer")
    print("almindelig python løkke")
    for line in a1:
      for item in line:
        print(item," ",end="")
    print("")
    print("nditer går alle igennem i een løkke")
    for item in np.nditer(a1):
      print(item, " ", end="")
    print("")
    print("nditer anvender oprindelig layout af a1. Ved transponering henvises fortsat til dette layout")
    for item in np.nditer(np.transpose(a1)):
      print(item, " ", end="")
    print("")
    print("Ved copy laves et nyt array og med layout som det transponerede.")
    for item in np.nditer(np.transpose(a1).copy()):
      print(item, " ", end="")
    print("")
    print("dates in numpy")
    d = np.datetime64('2018-10-16 22:10:45')  # YYYY-MM-DD HH-mm-ss
    print("basisformat",d)
    date = np.datetime64(d, 'D')
    print("YYYY-MM-DD",date)
    print("itemized",date.item())
    dateitem=date.item()
    print("year",dateitem.year)
    print("month",dateitem.month)
    print("day",dateitem.day)
    month=np.datetime64(d, 'M')
    print(month)
    year=np.datetime64(d, 'Y')
    print(year)


# start of end skal være numpy datoerobjekter
start_date = np.datetime64('2018-10-16')
end_date = np.datetime64('2018-10-22')
datoserie=np.arange(start_date, end_date)
print("datoserie-numpy")
print(datoserie)


class lav_np():
  def __init__(self):
    self.koer()
  def koer(self):
    d=np.random.rand(3,3)*100
    print("tilfældige floats 0-100. print format")
    np.set_printoptions(formatter={'float': '{:>2.2f}'.format})
    print(d)
    for line in d: print(line)
    di=np.random.randint(10,20, size=(3,3))
    print("random integer fra 10 ti 19")
    print(di)
    print("nuller, ettaller og diagonal")
    print("en dim",np.zeros(3))
    print(np.zeros((3,3)))
    print("en dim - ettaller",np.ones(3))
    print(np.ones((3,3)))
    print("diagonal")
    print(np.eye(3))
    print(np.identity(3,dtype=int))
    print("shift diagonal")
    print(np.eye(3,k=-1,dtype=int))


class sliceindex():
  def __init__ (self,a,b):
    self.a=a
    self.b=b
    self.pick() 

  def pick(self):
    a1=self.a
    b1=self.b
    print("vælg række",a1[2])
    print("vælg søjle",a1[:,1])
    print("vælg enkelt elementer fra række",a1[1,(0,2)])
    print("vælg interval af elementer fra række",a1[1,0:2])
    print("vælg enkelt elementer fra søjle",a1[(0,2),2])
    print("vælg interval af elementer fra søjle",a1[0:2,0])

class sumetc():
  def __init__(self,a,b):
    self.a=a
    self.b=b
    self.regn()

  def regn(self):
    a1=self.a
    b1=self.b
    print(" pi og e")
    print(np.pi, np.e)
    print("print by iteration")
    for line in a1: print(line)
    print("sum")
    print("hele array",a1.sum())
    print("første række",a1[0].sum())
    print("anden kolonne",a1[:,1].sum())

    print("print by iteration-multiple assignment")
    for (x,y,z) in a1: print(x+y+z) # x,y,z er elementer i linie. parentesen giver en linie
    for line in a1:print(line.sum())

    print("produkt")
    print("hele array",a1.prod())
    print("første række",a1[0].prod())

    print("Gennemsnit")
    print("hele array",a1.mean())
    print("første række",a1[0].mean())

    print("Minimum")
    print("hele array",a1.min())
    print("første række",a1[0].min())

    print("Index for minimum")
    print("hele array",a1.argmin())
    print("første række",a1[0].argmin())

    print("Index for værdi")
    indexud=np.where(abs(a1)>=5)
    for line in indexud: print(line)
    print(indexud)
    print(len(indexud[0])) #giver antal fundne
    print(indexud[0][:4]) #første liste er x-værdier i array. anden liste y værdier. Så [0] giver linie med x værdier. [:4] giver x værdier under 4

class combinere():
  def __init__(self,a,b):
    self.a=a
    self.b=b
    self.regn()

  def regn(self):
    #deep copy. Så kan vi resette a1 og b1
    a1=self.a.copy()
    b1=self.b.copy()

    print("kombinere i rækker")
    print(np.concatenate((a1,b1)))
    print("kombinere i søjler")
    print(np.concatenate((a1,b1),axis=1))
    print("lægge een række fra anden array til i søjler")
    #lav række et til søjle. 
    c1=b1[0].reshape(-1,1) #med -1 behøver man ikke angive længde. Bare til slutning.
    print(np.concatenate((a1,c1),axis=1))
    print("lægge een søjle fra anden array til i søjler")
    c2=b1[:,:1] #resultat af slicing er et array hvis der kun er een søjle valgt.med :1 sikrer at søjleformat bibeholdes
    print(np.concatenate((a1,c2),axis=1))

    print("summere to søjler fra et array og lægge sum til i søjle i andet array")
    c3=b1[:,:2] # Vi vælger 2 søjle 0-1
    print(c3)
    c4=np.sum(c3, axis=1).reshape(-1,1)
    print(c4)
    print(np.concatenate((a1,c4),axis=1))

    print("multiplicere søjle med tal")
    tal=3
    print(a1)
    a1[:,1]*=tal
    print(a1)      
    a1=self.a.copy() #nulstil a1

    print("multiplicere række med tal")
    tal=4
    print(a1)
    a1[1]*=tal
    print(a1)
    a1=self.a.copy() #nulstil a1

    print("sortere array efter kolonne")
    #Argsort giver en liste af index af leddene
    # Det er muligt at anvende boolean selection i numpy#Her angives som argument en liste af index for det som ønskes i output.
    # For eksempel giver a1[[2, 0, 1]] elementerne i a1 (rækker hvis matrix) i rækkefølge efter index. 3 elemnt først, så første og så andet.
    print(a1)
    print("argsort",a1[:,1].argsort()) # der sorteres efter kolonne 2 (nr 1)
    print(a1[a1[:,1].argsort()]) # rækkerne byttes

    print("sortere array efter række")
    print(a1)
    print("argsort",a1[2,:].argsort()) # der sorteres efter række 3 (nr 2)
    print(a1[:,a1[2,:].argsort()]) #søjlerne byttes derfor a1[:,

a= [[rd.randrange(1,10) if rd.randrange(2)==0 else -rd.randrange(1,10) for i in range(3)] for j in range(3)]
b=[[rd.randrange(1,10) if rd.randrange(2)==0 else -rd.randrange(1,10) for i in range(3)] for j in range(3)]

print("a",a) 
print("b",b)


a1=np.array(a) 
b1=np.array(b)
p1=np.random.randint(3,size=(3,3))  # random 0,1,2 dimension 3x3

npbasic(a1,b1,p1)

#lav_np()

#sliceindex(a1,b1)

#sumetc(a1,b1)
#combinere(a1,b1)


