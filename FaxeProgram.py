
import numpy as np
import csv
import time

class db_calculation():
  def __init__ (self, db, **filters):
    self.skemafil=[]
    self.db=db
    self.nulstil_filtre()
    for key, value in filters.items():
      self.filters_to_funktion(key,value) 
    self.beregn_samlet_filter()
    self.skema()

  def nulstil_filtre(self):
    self.f_yr=[]
    self.f_mo=[]
    self.f_na=[]
    self.f_di=[]
    self.f_co=[]
    self.f_cu=[]
    self.f_sh=[]
    self.f_ma=[]
    self.f_pr=[]
    self.f_md=[]
 
    self.f_ytd=[]

  def skema(self):
    return self.skemafil

  def filters_to_funktion(self,navn,value):
    valg={"yr":self.yr,"mo":self.mo,"na":self.na,"di":self.di,"co":self.co,"cu":self.cu,"sh":self.sh,"ma":self.ma,"pr":self.pr,"md":self.md}
    funktion=valg.get(navn)
    funktion(value)
  
  def beregn_filter(self,basefilter,periodfilter):
    filtertotal=np.logical_and(basefilter,periodfilter)       
    if len(self.f_na)>0:
      filtertotal=np.logical_and(filtertotal,self.f_na)
    if len(self.f_di)>0:
      filtertotal=np.logical_and(filtertotal,self.f_di)
    if len(self.f_co)>0:
      filtertotal=np.logical_and(filtertotal,self.f_co)    
    if len(self.f_cu)>0:
      filtertotal=np.logical_and(filtertotal,self.f_cu)
    if len(self.f_sh)>0:
      filtertotal=np.logical_and(filtertotal,self.f_sh)
    if len(self.f_ma)>0:
      filtertotal=np.logical_and(filtertotal,self.f_ma)
    if len(self.f_pr)>0:
      filtertotal=np.logical_and(filtertotal,self.f_pr)
    if len(self.f_md)>0:
      filtertotal=np.logical_and(filtertotal,self.f_md)
    
    return filtertotal
  
  def beregn_samlet_filter(self):

    self.f_total_mo=self.beregn_filter(self.f_mo,self.f_yr)
    self.f_total_ytd=self.beregn_filter(self.f_ytd,self.f_yr)
    self.f_total_last_mo=self.beregn_filter(self.f_mo,self.f_last_yr)
    self.f_total_last_ytd=self.beregn_filter(self.f_ytd,self.f_last_yr)
    
    db_mo=self.db[self.f_total_mo]
    db_ytd=self.db[self.f_total_ytd]
    db_last_mo=self.db[self.f_total_last_mo]
    db_last_ytd=self.db[self.f_total_last_ytd]

    #print(np.sum(db_mo["actual"]),np.sum(db_mo["budget"]),np.sum(db_last_mo["actual"]),np.sum(db_ytd["actual"]),np.sum(db_ytd["budget"]),np.sum(db_last_ytd["actual"]))

    self.skemafil.append([np.sum(db_mo["actual"]),np.sum(db_mo["budget"]),np.sum(db_last_mo["actual"]),np.sum(db_ytd["actual"]),np.sum(db_ytd["budget"]),np.sum(db_last_ytd["actual"])])
  
  def yr(self,v):
    aar=v
    self.f_yr=np.isin(db["year"],aar)
    self.f_last_yr=np.isin(db["year"],aar-1)

  def mo(self,v):
    maaned=v
    ytd=[i for i in range(1,maaned+1)]
    self.f_mo=np.isin(db["month"],maaned)
    self.f_ytd=np.isin(db["month"],ytd)
    
  def na(self,v):
    nat=v
    self.f_na=np.isin(db["nature"],nat)
    #Hvis ingen betingelser skal alle være True og listen inverteres
    if nat==[]: self.f_na=np.logical_not(self.f_na)
          
  def di(self,v):
    dist=v
    self.f_di=np.isin(db["distr"],dist)
    #Hvis ingen betingelser skal alle være True og listen inverteres
    if dist==[]: self.f_di=np.logical_not(self.f_di)

  def co(self,v):
    country=v
    self.f_co=np.isin(db["country"],country)
    #Hvis ingen betingelser skal alle være True og listen inverteres
    if country==[]: self.f_co=np.logical_not(self.f_co)

  def cu(self,v):
    cus=v
    self.f_cu=np.isin(db["customer"],cus)
    #Hvis ingen betingelser skal alle være True og listen inverteres
    if cus==[]: self.f_cu=np.logical_not(self.f_cu)

  def sh(self,v):
    shto=v
    self.f_sh=np.isin(db["shipto"],shto)
    #Hvis ingen betingelser skal alle være True og listen inverteres
    if shto==[]: self.f_sh=np.logical_not(self.f_sh)

  def ma(self,v):
    mat=v
    self.f_ma=np.isin(db["material"],mat)
    #Hvis ingen betingelser skal alle være True og listen inverteres
    if mat==[]: self.f_ma=np.logical_not(self.f_ma)

  def pr(self,v):
    pro=v
    self.f_pr=np.isin(db["process"],pro)
    #Hvis ingen betingelser skal alle være True og listen inverteres
    if pro==[]: self.f_pr=np.logical_not(self.f_pr)

  def md(self,v):
    mdu=v
    self.f_md=np.isin(db["mduse"],mdu)
    #Hvis ingen betingelser skal alle være True og listen inverteres
    if mdu==[]: self.f_md=np.logical_not(self.f_md)

class importfiles():

  def __init__(self):
    pass

  def kriteriefil(self):
    kriterier=[]
    with open("KriterierExcelGammelCSV.csv") as f:
      for line in f:
        line=line.strip('\n')
        #print(line.split(';'))
        kriterier.append(line.split(';'))
    return kriterier

  def datafil(self):
    #Prepare excel file: 1)change all # to NA. 2) Slet overskrifter 3) save as tabseparated
    dt=np.dtype([("nature",'U10'),("distr",'U10'),("country",'U10'),("customer",'i4'),("shipto",'i4'),("material",'i4'),("process",'U10'),("mduse",'U10'),("year",'i4'),("month",'i4'),("actual",'f4'),("budget",'f4')])
    db=np.genfromtxt("FaxeDataStorTab1.txt",delimiter='\t',dtype=dt)

    db["actual"][np.isnan(db["actual"])] = 0
    db["budget"][np.isnan(db["budget"])] = 0

    return db

def sumlinier(mitskema,addlinier):
  antalcol=len(mitskema[0][0])
  print(antalcol,"antalkolonner")
  sumresult=[0 for i in range(antalcol)]
  deflinier=[abs(int(item)) for item in addlinier.split(' ')]
  sign=[-1 if int(item)<0 else 1 for item in addlinier.split(' ')]
  print(deflinier,sign,"her er rutine til sumlinie")
  for col in range(antalcol):
    for nr,item in enumerate(deflinier):
      sumresult[col]+=mitskema[item-1][0][col]*sign[nr]
  return sumresult


   

def beregnskema(db,kriterier):
  mitskema=[]

  #Skemaet gennemgås nu per linie
  antalcol=len(kriterier[0])
  antallin=len(kriterier)

  for line in range(1,antallin):
    year=int(kriterier[line][3])
    maaned=int(kriterier[line][4])

    if not kriterier[line][2]:
    
      if kriterier[line][5]: # is false if empty
        nature=kriterier[line][5]
        nature=[item for item in nature.split(' ')] 
      else: nature=[]
      
      if kriterier[line][6]:
        dist=kriterier[line][6]
        dist=[item for item in dist.split(' ')]
      else: dist=[]

      if kriterier[line][7]:
        country=kriterier[line][7]
        country=[item for item in country.split(' ')]
      else: country=[]

      if kriterier[line][8]:
        cus=kriterier[line][8]
        cus=[int(item) for item in cus.split(' ')]
      else: cus=[]

      if kriterier[line][9]:
        shto=kriterier[line][9]
        shto=[int(item) for item in shto.split(' ')]
      else: shto=[]

      if kriterier[line][10]:
        mat=kriterier[line][10]
        mat=[int(item) for item in mat.split(' ')]
      else: mat=[]

      if kriterier[line][11]:
        pro=kriterier[line][11]
        pro=[item for item in pro.split(' ')]
      else: pro=[]

      if kriterier[line][12]:
        mdu=kriterier[line][12]
        mdu=[item for item in mdu.split(' ')]
      else: mdu=[]


      print(year,maaned,nature,dist,mat,pro)

      #db_calculation(db,yr=year,mo=maaned,na=nature,di=dist,co=country,cu=cus,sh=shto,ma=mat,pr=pro,md=mdu).skema()

      mitskema.append(db_calculation(db,yr=year,mo=maaned,na=nature,di=dist,co=country,cu=cus,sh=shto,ma=mat,pr=pro,md=mdu).skema())

      #line text sum year month nature dist country customer shipto material process mduse

    else:
      mitskema.append([])
      print(line,"dette er en sumkolonne")

  
  sumdef=[line[2] for line in kriterier]
  del sumdef[0]
  print(sumdef)
  for nr,line in enumerate(mitskema):
    if not line:
      linie=sumlinier(mitskema,sumdef[nr])
      mitskema[nr]=[[item for item in linie]]
  return mitskema



#=================================
#===========Hovedprogram===========

f=importfiles()
db=f.datafil()
kriterier=f.kriteriefil()
skema=beregnskema(db,kriterier)

start=time.time()
for line in skema:
  print("")
  for item in line[0]:
    print('{:8.1f}'.format(item),end="")
end=time.time()
print("")
print("time taken", '{:10.4f}'.format(1000*(end-start)))




