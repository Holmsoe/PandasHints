import pandas as pd
import numpy as np
import copy

def indlaesdata():
  with open("FaxeDataStorTab1.txt") as f:
    db=[]
    for line in f:
      line=line.strip('\n')
      db.append(line.split('\t'))

  for line in db:
    if len(line[10])==0: line[10]='0'
    if len(line[11])==0: line[11]='0'
  return db

def indlaeskriterie():
  kriterier=[]
  with open("KriterierCSV3.csv") as f:
    for line in f:
      line=line.strip('\n')
      kriterier.append(line.split(','))
    return kriterier

def make_query(kt):
  '''
  The query is constructed by conditions which are not empty (if kt[j][i]!=['']).
  conditions for separate colums are joined by "and" ('and '.join([kolonner[i+1])
  The name of the column is taken from dictinary kolonner based on column number (i+1)
  Table is looped by number of columnswith conditions (len(kt[0])) - not including data columns (actual,budget)
  Conditions per column are given as list. In case there are several options the list in text for the query is done with ("','".join(kt[j][i])). In order to make sure that letter are recognize as text and not variable the comma is enclosed by '. Furter a ' is given at each end (+"'")
  Example of query: 
  process in ['Milled','Drying'] and year in ['2019'] and month in ['6']
  '''
  q='and '.join([kolonner[i+1]+" in ["+"'" +"','".join(kt[j][i])+"'"+"] " for i in range(0,len(kt[0])) if kt[j][i]!=[''] ])

  return q 


db=indlaesdata()
#for line in db[:5]: print(line)

kt=indlaeskriterie()
#Delete titles
del kt[0] 
#Transfer column with info on lines calculated from other lines
sumline=[line[2] for line in kt]
#Transfer text for line
textline=[line[1] for line in kt]

#Delete 3 first columns: linenr, text, sumline info
for line in kt: 
  del line[0:3]

#Split criteras with more than one input
#Will also convert single criteria to list format
#This is criterias for the actual month/year
kt_mth=[[item.split(' ') for item in line] for line in kt]

#for line in kt_mth: print(line)

#Get year and month
act_year=int(kt_mth[0][8][0])
act_mth=int(kt_mth[0][9][0])
last_year=act_year-1

#Correct criterias to last year - column 8 with year.
#[0] is necessary because year is a list with one member
kt_lyr=copy.deepcopy(kt_mth)
for line in kt_lyr: line[8][0]=str(last_year)

#Correct criterias to ytd - column 9 with year.
#A list with month from 1 to actual is inserted
kt_ytd=copy.deepcopy(kt_mth)
ytd_list=[str(i) for i in range(1,act_mth+1)]
for line in kt_ytd: line[9]=ytd_list

#Correct criterias to last year ytd 
#Based on ytd and only year is corrected from actual to last.
kt_lyr_ytd=copy.deepcopy(kt_ytd)
for line in kt_lyr_ytd: line[8][0]=str(last_year)

col=["nature", "dist", "country", "customer", "shipto", "material", "process", "mduse", "year", "month", "actual", "budget"]

kolonner={1:"nature",2:"dist",3:"country",4: "customer",5: "shipto",6: "material",7: "process",8: "mduse",9: "year",10: "month",11: "actual",12: "budget"}

df=pd.DataFrame(db,columns=col)

df[["customer","shipto","material","year","month","actual","budget"]] = df[["customer","shipto","material","year","month","actual","budget"]].apply(pd.to_numeric, errors='coerce')

skema=[]
#for line in kt_mth: print(line)
#print(sumline)
for j in range(0,len(kt_mth)):
  if sumline[j]=='':
    q_mth=make_query(kt_mth)
    q_lyr=make_query(kt_lyr)
    q_ytd=make_query(kt_ytd)
    q_lyr_ytd=make_query(kt_lyr_ytd)

    df_mth=df.query(q_mth)
    #if j==0: 
       #print(df_mth[["material","actual","budget"]].head(20))

    df_lyr=df.query(q_lyr)
    df_ytd=df.query(q_ytd)
    df_lyr_ytd=df.query(q_lyr_ytd)

    skema.append([df_mth["actual"].sum(),df_mth["budget"].sum(),df_lyr["actual"].sum(),df_ytd["actual"].sum(),df_ytd["budget"].sum(),df_lyr_ytd["actual"].sum()])
  else:
    skema.append([0,0,0,0,0,0])

for nr,line in enumerate(skema): line.insert(0,textline[nr])
for line in skema: print('{:20}{:10.1f}{:10.1f}{:10.1f}{:10.1f}{:10.1f}{:10.1f}'.format(*line))



