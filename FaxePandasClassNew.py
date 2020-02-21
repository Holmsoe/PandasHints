import pandas as pd
import copy

#=================START===================================
class PrepareData():

  def __init__(self,db_file,krit_file):
    self.ReadDatabase(db_file)
    self.ReadCriteria(krit_file)
    self.PrepareDatabase()
    self.PrepareCriteria()

  def ReadDatabase(self,db_name):
    self.db=[]
    with open(db_name) as f:
      for line in f:
        line=line.strip('\n')
        self.db.append(line.split('\t'))

  def ReadCriteria(self,krit_name):
    self.kt=[]
    with open(krit_name) as f:
      for line in f:
        line=line.strip('\n')
        self.kt.append(line.split(','))

  def PrepareDatabase(self):

    self.col_names=["nature", "dist", "country", "customer", "shipto", "material", "process", "mduse", "year", "month", "actual", "budget"]

    self.db_pd=pd.DataFrame(self.db,columns=self.col_names)
    self.db_pd[["customer","shipto","material","year","month","actual","budget"]] = self.db_pd[["customer","shipto","material","year","month","actual","budget"]].apply(pd.to_numeric, errors='coerce')
    
  def PrepareCriteria(self):
    #Delete titles
    del self.kt[0] 
    #Save data in first two columns
    self.sumline=[line[2] for line in self.kt]
    self.textline=[line[1] for line in self.kt]
    #Delete 3 first columns: linenr, text, sumline info
    for line in self.kt: 
      del line[0:3]
    #Split criteras with more than one input
    #Will also convert single criteria to list format
    self.kt=[[item.split(' ') for item in line] for line in self.kt]

    #Aktuel måned
    self.act_mth=int(self.kt[0][9][0])
    #Aktuel år
    self.act_year=int(self.kt[0][8][0])

    for line in self.kt: 
      del line[-2:]

  def GetDatabase(self):
    return self.db_pd
  
  def GetCriteria(self):
    return self.kt

  def Year(self):
    return self.act_year

  def Month(self):
    return self.act_mth

  def Sumline(self):
    return self.sumline

  def Textline(self):
    return self.textline

class FilterDatabase():
  def __init__(self,database,actual_line_criteria):
    self.db_ind=database
    self.kt_line=actual_line_criteria
    self.col_list={1:"nature",2:"dist",3:"country",4: "customer",5: "shipto",6: "material",7: "process",8: "mduse",9: "year",10: "month",11: "actual",12: "budget"}
    

  def make_query(self):
    '''
    Beregner kriterie som tekst for een kriterielinie
    kt_line er kriterie for aktuel linie.
    The query is constructed by conditions which are not empty (if kt_line[i]!=['']).
    Conditions for separate colums are joined by "and" ('and '.join([self.col_list[i+1])
    The name of the column is taken from dictinary kolonner based on column number (i+1)
    Table is looped by number of columnswith conditions (len(kt_line)) - not including data columns (actual,budget)
    Conditions per column are given as list. In case there are several options the list in text for the query is done with ("','".join(kt_line[i])). In order to make sure that letter are recognize as text and not variable the comma is enclosed by '. Further a ' is given at each end (+"'")
    Example of query: 
    process in ['Milled','Drying'] and year in ['2019'] and month in ['6']
    '''
    q='and '.join([self.col_list[i+1]+" in ["+"'" +"','".join(self.kt_line[i])+"'"+"] " for i in range(0,len(self.kt_line)) if self.kt_line[i]!=[''] ])
    return q

class Tabel3col():
  def __init__(self,dbname,ktname):
    self.db_name=dbname
    self.kt_name=ktname
    self.BeregnSkema()

  def sumlinier(self,mitskema,sumlinie):
    antalcol=len(mitskema[0])
    sumresult=[0 for i in range(antalcol)]
    linier_i_sum=[abs(int(item)) for item in sumlinie.split(' ')]
    sign_per_linie=[-1 if int(item)<0 else 1 for item in sumlinie.split(' ')]
    for col in range(antalcol):
      for nr,item in enumerate(linier_i_sum):
        sumresult[col]+=mitskema[item-1][col]*sign_per_linie[nr]
    return sumresult
    

  def BeregnSkema(self):

    minedata=PrepareData(self.db_name,self.kt_name)
    db=minedata.GetDatabase() 
    kt=minedata.GetCriteria()
    sumline=minedata.Sumline() 
    textline=minedata.Textline() 
    yr=minedata.Year()
    mth=minedata.Month()

    skema=[]

    for linenr,kt_line in enumerate(kt):
      if sumline[linenr]=="":
        mitFilter=FilterDatabase(db,kt_line)
        f=mitFilter.make_query()
        df=db.query(f)

        df_mth=df[(df["year"]==yr) & (df["month"]==mth)]
        df_lyr=df[(df["year"]==yr-1) & (df["month"]==mth)]
        df_ytd=df[(df["year"]==yr) & (df["month"]<=mth)]
        df_lyr_ytd=df[(df["year"]==yr-1) & (df["month"]<=mth)]
        
        skema.append([df_mth["actual"].sum(),df_mth["budget"].sum(),df_lyr["actual"].sum(),df_ytd["actual"].sum(),df_ytd["budget"].sum(),df_lyr_ytd["actual"].sum()])
      else:
        skema.append([0,0,0,0,0,0])
    for nr,line in enumerate(skema):
      if sumline[nr]!="":
        #print("før",line)
        skema[nr]=self.sumlinier(skema,sumline[nr])
        

    for nr,line in enumerate(skema):
      line.insert(0,textline[nr])
    for line in skema:
      print('{:20}{:10.1f}{:10.1f}{:10.1f}{:10.1f}{:10.1f}{:10.1f}'.format(*line))  


db_name="FaxeDataStorTab1.txt"
kt_name="KriterierCSV3.csv"

mintabel=Tabel3col(db_name,kt_name)



