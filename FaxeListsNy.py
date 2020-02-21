def indlaesdata():
  with open("FaxeDataStorTab1.txt") as f:
    db=[]
    for line in f:
      line=line.strip('\n')
      db.append(line.split('\t'))
  return db

def indlaeskriterie():
  kriterier=[]
  with open("KriterierCSV3.csv") as f:
    for line in f:
      line=line.strip('\n')
      kriterier.append(line.split(','))
  return kriterier

def db_period(db_full,yr,mth,ytd_boolean):
  '''
  Beregn filtreret database med actual med måned og år. Hvis ytd_boolean er falsk beregnes Kune aktuel måned eller år tid dato tal.
  '''
  if not ytd_boolean:
    db_ud=[line for line in db_full if line[-4]==yr and line[-3]==mth]
  else:
    db_ud=[line for line in db_full if line[-4]==yr and int(line[-3])<=int(mth)]
  return db_ud

def db_filter(db,k_line):
  '''
  Beregn reduceret database med aktuel filterlinie (excl måned og år). 
  Kalder filtervalue med aktuel linie og kondition. Filtervalue fortæller om linien medtages eller ej.
  '''
  db_ud=[line for line in db if filtervalue(line,k_line)]
  return db_ud

def filtervalue(db_line,kt_line):
  '''
  Tjekker om linien fra databasen overholder filter kondition. Felterne i database og filter er modsvarende . Derfor kan de gennemgås med en løkke. Hvis ikke en af felter er OK bliver konditionen falsk. Bemærk at konditionen for et felt kan indholde flere værdier. Derfor undersøged om den aktuelle feltværdien er indholdt heri.
  '''
  ud=True
  for i in range(8):
    if kt_line[i]!=[""]:
      if db_line[i] not in kt_line[i]:
        ud=False
  return ud

def db_sum(db,valg):
  '''
  Beregner sum af de 2 sidste kolonner i database. Hvis valg=actual så beregnes næstsidste søjle-eller sidste.
  '''
  if valg=="actual":
    return sum([float(line[-2]) for line in db if line[-2]!=""])
  else:
    return sum([float(line[-1]) for line in db if line[-1]!=""])

def sumlinier(mitskema,sumlinie):
  antalcol=len(mitskema[0])
  sumresult=[0 for i in range(antalcol)]
  linier_i_sum=[abs(int(item)) for item in sumlinie.split(' ')]
  sign_per_linie=[-1 if int(item)<0 else 1 for item 
  in sumlinie.split(' ')]
  for col in range(1,antalcol):
    for nr,item in enumerate(linier_i_sum):
      sumresult[col]+=mitskema[item-1][col]*sign_per_linie[nr]
  return sumresult

def beregn_skema(yr,mth,db_full,kr_full):
  kr=[line[3:] for line in kr_full]
  yr=kr[4][-2]
  mth=kr[4][-1]
  lyr=str(int(yr)-1)
  
  db_mth_period=db_period(db_full,yr,mth,False)
  db_ytd_period=db_period(db_full,yr,mth,True)
  db_lyr_period=db_period(db_full,lyr,mth,False)
  db_lyr_ytd_period=db_period(db_full,lyr,mth,True)

  skema=[]

  for i in range(1,len(kr)):
    k_line=[item.split(' ') for item in kr[i]]
    k_line1=kr[i]

    db_mth=db_filter(db_mth_period,k_line)
    db_ytd=db_filter(db_ytd_period,k_line)
    db_lyr=db_filter(db_lyr_period,k_line)
    db_lyr_ytd=db_filter(db_lyr_ytd_period,k_line)

    skema.append([db_sum(db_mth,"actual"),db_sum(db_mth,"budget"),db_sum(db_lyr,"actual"),db_sum(db_ytd,"actual"),db_sum(db_ytd,"budget"),db_sum(db_lyr_ytd,"actual")])

  for nr,line in enumerate(skema):
    line.insert(0,kr_full[nr+1][1])

  sumline=[line[2] for line in kr_full]
  del sumline[0]
  for nr,line in enumerate(skema):
    if nr>0 and sumline[nr]!="":
      #print("før",line)
      tekst=skema[nr][0]
      skema[nr]=sumlinier(skema,sumline[nr])
      skema[nr][0]=tekst

  return skema

#===================HOVEDPROGRAM=============================
db=indlaesdata()
kr=indlaeskriterie()
yr=kr[4][-2]
mth=kr[4][-1]

skema=beregn_skema(yr,mth,db,kr)

for line in skema:
  print('{:20}{:10.1f}{:10.1f}{:10.1f}{:10.1f}{:10.1f}{:10.1f}'.format(*line))

