import pandas as pd
import copy

#=================START===================================
class PrepareData():
  '''
  A. Indlæsning
  Indlæser database og kriterietabel og tilpasser listerne
  Database er gemt som tabulatorsepareret. CSV giver problemer pga. af kommaer i nogle tal.
  Kriterier er gemt som csv
  B. Tilpasning af kriteriedata.
  Overskrift fjernes.
  Kolonnne 0 er linienummerering.
  Kolonne nr 1+2 , med hhv tekst og definition af sum for linier der beregnes fra andre linier, indlæses i separate lister.
  Herefter slettes de tre første kolonner.
  C. Overførsel til liste af basiskriterie som svarer til den aktuelle måned og år. Bemærk, at kolonner kan have flere gyldige værdier. for eksempel 3 materialenumre. 
  Format på kriterie linie: [[""],[52,34],['B'],....]
  Hvis der ikke er condition for kolonne er indholdet en liste med "".
  Hvis der een værdi er indholdet en liste med værdien og ikke blot værdien.
  Hele kritiesættet for alle linier består af en liste med ovenstående "liste af liste". Et kriterie per linie
  D. Endelig korrigeres basiskriterie.
  Der laves kriterier for Aktuel måned/Aktuel år (basis), Aktuel år/year to date, Sidste år/aktuel måned, Sidste år/Year to date.
  E. Database, kriterier

  '''
  def __init__(self,db_file,krit_file):
    self.ReadDatabase(db_file)
    self.ReadCriteria(krit_file)
    self.MakeMonthCriteria(self.kriterier)

  def ReadDatabase(self,db_name):
    self.db=[]
    with open(db_name) as f:
      for line in f:
        line=line.strip('\n')
        self.db.append(line.split('\t'))

  def ReadCriteria(self,krit_name):
    self.kriterier=[]
    with open(krit_name) as f:
      for line in f:
        line=line.strip('\n')
        self.kriterier.append(line.split(','))

  def MakeMonthCriteria(self,kt):
    '''
    basiskriterie for aktuel år og måned: self.kt_mth
    '''
    #Delete titles
    del kt[0] 
    #Save data in first two columns
    self.sumline=[line[2] for line in kt]
    self.textline=[line[1] for line in kt]
    #Delete 3 first columns: linenr, text, sumline info
    for line in kt: 
      del line[0:3]
    #Split criteras with more than one input
    #Will also convert single criteria to list format
    self.kt_mth=[[item.split(' ') for item in line] for line in kt]

    #Aktuel måned
    self.act_mth=int(self.kt_mth[0][9][0])
    #Aktuel år
    self.act_year=int(self.kt_mth[0][8][0])
    #Sidste år
    self.last_year=self.act_year-1

  def GetDatabase(self):
    return self.db

  def GetCriteria(self):
    return self.kriterier

  def GetMthCrit(self):
    return self.kt_mth

  def GetLyrCrit(self):
    #Correct criterias to last year - column 8 with year.
    #[0] is necessary because year is a list with one member
    self.kt_lyr=copy.deepcopy(self.kt_mth)
    for line in self.kt_lyr: line[8][0]=str(self.last_year)
    return self.kt_lyr

  def GetYTDCrit(self):
    #Correct criterias to ytd - column 9 with year.
    #A list with month from 1 to actual is inserted
    self.kt_ytd=copy.deepcopy(self.kt_mth)
    ytd_list=[str(i) for i in range(1,self.act_mth+1)]
    for line in self.kt_ytd: line[9]=ytd_list
    return self.kt_ytd

  def GetLyrYTDCrit(self):
    #Correct criterias to last year ytd 
    #Based on ytd and only year is corrected from actual to last.
    self.kt_lyr_ytd=copy.deepcopy(self.kt_ytd)
    for line in self.kt_lyr_ytd: line[8][0]=str(self.last_year)
    return self.kt_lyr_ytd

  def GetSumline(self):
    return self.sumline

  def GetText(self):
    return self.textline

  def GetActualMonth(self):
    return self.act_mth

  def GetActualYear(self):
    return self.act_year

#=================SLUT===================================

#=================START===================================

class FilterDatabase():
  def __init__(self,database,actual_line_criteria):
    self.db_ind=database
    self.actual_criteria=actual_line_criteria
    self.PrepareDatabase()

  def PrepareDatabase(self):

    self.col_names=["nature", "dist", "country", "customer", "shipto", "material", "process", "mduse", "year", "month", "actual", "budget"]

    self.col_list={1:"nature",2:"dist",3:"country",4: "customer",5: "shipto",6: "material",7: "process",8: "mduse",9: "year",10: "month",11: "actual",12: "budget"}

    self.db=pd.DataFrame(self.db_ind,columns=self.col_names)

    self.db[["customer","shipto","material","year","month","actual","budget"]] = self.db[["customer","shipto","material","year","month","actual","budget"]].apply(pd.to_numeric, errors='coerce')

  def make_query(self,kt_line):
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
    q='and '.join([self.col_list[i+1]+" in ["+"'" +"','".join(kt_line[i])+"'"+"] " for i in range(0,len(kt_line)) if kt_line[i]!=[''] ])
    return q 

  def GetMthDatabase(self):
    act_query=self.make_query(self.actual_criteria)
    self.db_mth=self.db.query(act_query)
    return self.db_mth

  def GetLyrDatabase(self):
    act_query=self.make_query(self.actual_criteria)
    self.db_lyr=self.db.query(act_query)
    return self.db_lyr

  def GetYTDDatabase(self):
    act_query=self.make_query(self.actual_criteria)
    self.db_ytd=self.db.query(act_query)
    return self.db_ytd

  def GetLyrYTDDatabase(self):
    act_query=self.make_query(self.actual_criteria)
    self.db_lyr_ytd=self.db.query(act_query)
    return self.db_lyr_ytd

#=================SLUT===================================

#=================START===================================

class MakeTable3Col():
  def __init__(self,dbname,ktname):
    self.dbname=dbname
    self.ktname=ktname
    self.GetData()
    self.BeregnLinier()

  def GetData(self):
    self.minedata=PrepareData(self.dbname,self.ktname)
    #Sumdefinition for linier der findes som sum af andre linier
    self.sumline=self.minedata.GetSumline()
    #Tekst per linie
    self.textline=self.minedata.GetText()
    #Database
    self.db=self.minedata.GetDatabase()
    #Kriterier 
    #Aktuel måned og år. En for hver linie 
    self.kt_mth=self.minedata.GetMthCrit()
    #Aktuel måned men år er aktuel minus 1
    self.kt_lyr=self.minedata.GetLyrCrit() 
    #YTD alle måneder i aktuelt år til og med aktuel måned
    self.kt_ytd=self.minedata.GetYTDCrit() 
    #YTD sidste år. Alle måneder til og med aktuel for sidste år.
    self.kt_lyr_ytd=self.minedata.GetLyrYTDCrit()
  
  def BeregnLinier(self):
    skema=[]
    for j in range(0,len(self.sumline)):
      if self.sumline[j]=='':

        self.db_mth=FilterDatabase(self.db,self.kt_mth[j]).GetMthDatabase()
        self.db_lyr=FilterDatabase(self.db,self.kt_lyr[j]).GetLyrDatabase()
        self.db_ytd=FilterDatabase(self.db,self.kt_ytd[j]).GetYTDDatabase()
        self.db_lyr_ytd=FilterDatabase(self.db,self.kt_lyr_ytd[j]).GetLyrYTDDatabase()

        skema.append([self.db_mth["actual"].sum(),self.db_mth["budget"].sum(),self.db_lyr["actual"].sum(),self.db_ytd["actual"].sum(),self.db_ytd["budget"].sum(),self.db_lyr_ytd["actual"].sum()])
      else:
        skema.append([0,0,0,0,0,0])

    for nr,line in enumerate(skema): 
      line.insert(0,self.textline[nr])
    for line in skema: 
      print('{:20}{:10.1f}{:10.1f}{:10.1f}{:10.1f}{:10.1f}{:10.1f}'.format(*line))    

#=================SLUT===================================

#================HOVEDPROGRAM===========================
db_name="FaxeDataStorTab1.txt"
kt_name="KriterierCSV3.csv"

mintabel=MakeTable3Col(db_name,kt_name)


