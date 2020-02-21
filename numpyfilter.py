import numpy as np 
import random as rd 


db=np.array([[rd.randint(100001,100009),rd.randint(100,109),rd.random()*50,rd.random()*50,rd.random()*10] for i in range(10)])

def printdb(db):
  for line in db: print('{:6.0f}{:6.0f}{:6.2f}{:6.2f}{:6.2f}'.format(*line))

printdb(db)

print(np.sum(db[:,2]))
print(np.mean(db[:,2]))
print(np.min(db[:,2]))
print(np.max(db[:,2]))
print(np.argmin(db[:,2]))

#Sortering på kolonne-argsort
dbny=db.copy()
asort=np.argsort(dbny[:,2]) #sortering med kolonne 2
print("index for sorteret rækkefølge",asort)
db1=dbny[asort]
print("rækker byttes iht index for rækkefølge")
printdb(db1)

#Sortering efter række
#asort=np.argsort(dbny[2,:]) #sortering med række 2
#db2=dbny[:,asort]
#printdb(db2)

#sortering med 2 kolonner-lexsort
dbn=db.copy()
print("Sortere med 2 kolonner")
#kriterier med "baglæns" rækkefølge. Den sidste søjle er den højeste prioritet.
db4=dbn[np.lexsort((dbn[:,2], dbn[:,0]))]
printdb(db4)

#dtype test
print("Test dtype argsort anvendes til 2 kolonner filter")
#Her defineres datatyper per kolonne. Der gives et navn per kolonne
dt = np.dtype([('cust', np.int), ('mat', np.int),('vol',np.float),('pris',np.float),('log',np.float)])
#Her indlæses databasen i tuples med def af dtype
dbn2=np.array([(rd.randint(100001,100009),rd.randint(100,109),rd.random()*50,rd.random()*50,rd.random()*10) for i in range(10)],dtype=dt)
#Sorteringsrækkefølgen bestemmes baseret på kolonnenavne
xfilter=np.argsort(dbn2,order=('cust','vol'))
printdb(dbn2[xfilter])

#filter med kriterie på en kolonne
print("filter på kolonne")
db5=db[db[:,2]>20] #Alle rækker hvor kolonne 2>20
printdb(db5)

#filter med kriterie på flere kolonner AND
print("filter på 2 kolonner med AND")
afilter=np.logical_and(db[:,2]>20,db[:,4]>3) 
#Alle rækker hvor kolonne 2>20 og kolonne 4>3
db6=db[afilter]
printdb(db6)

#filter med OR 
print("filter med OR og sortering efter kolonne")
bfilter=np.logical_or(db[:,2]<20,db[:,2]>40)
db7=db[bfilter]
printdb(db7[np.argsort(db7[:,2])])

#filter med OR og AND 
print("filter med OR og AND og sortering efter kolonne")
cfilter=np.logical_or(db[:,2]<20,db[:,2]>40)
dfilter=np.logical_and(db[:,0]>100002,db[:,0]<100008)
efilter=np.logical_and(cfilter,dfilter)
db8=db[efilter]
printdb(db8[np.argsort(db8[:,2])])

# Filter med liste og isin og sortering efter kolonne og sum
print("filter liste og isin og sum af kolonne")
customervalg=[100003,100005,100008]
ffilter=np.isin(db[:,0],customervalg)
db9=db[ffilter]
printdb(db9[np.argsort(db9[:,2])])
print("sum af valg-kolonne 2",'{:6.2f}'.format(np.sum(db9[:,2])))

# Filter med 2 kriterier med lister sortering efter  2 kolonner
print("filter med 2 kriterier og sortering efter 2 kolonner")
customer=[100003,100005,100008]
material=[101,103,105,107,109]
f=np.logical_and(np.isin(db[:,0],customer),np.isin(db[:,1],material))
filterdb=db[f]
printdb(filterdb[np.lexsort((filterdb[:,2],filterdb[:,0]))])

