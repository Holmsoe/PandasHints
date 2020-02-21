import copy

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

def reducedfilter(krit):
  '''
  rutine til reduktion af kriterie til kun at omfatte de kolonner der indholder en begrænsning.
  Kriterier er på formen:
  [['','',''...''],....['','',''...'']]
  Der er i alt 13 kolonner per kriterie linie []
  [line text sum nature dist country customer shipto material process mduse year month]
  Første linie anvendes ikke. (tekst)
  Kolonne 0,1,2 er ikke kriterie. Kriterie starter fra kolonne 3.

  Input til denne rutine er kriterier på formen [[kriterie], kolonnenummer]
  så krit[0] er selvekriteriet.
  krit_mth=[[krline[3+i],0+i] for i in range(10)] kriterie format genereres i dbfilter_beregn

  Rutinen kaldes af filterloop hver gang der er et nyt kriterie
  '''
  actualfilter=[]
  for line in krit:
    #Hvis kriteriet ikke er tomt
    if line[0]: 
      try: 
        #Hvis der er mere end en mulighed per kolonne skal de splitte til liste.
        line[0]=line[0].split(' ')
      except:
        pass
      #Hvis kriteriet ikke er tomt lægges det til filtret 
      actualfilter.append(line)
      
  return actualfilter

def dbfilter(db,ftline):
  '''
  På basis af aktive filterkolonner sorteres database således at kun linier der opfylder konditionen medtages.
  Input er en database som kan være reduceret i forhold til udgangs database.
  [nature dist country customer shipto material process mduse year month actual budget]
  samt reduceret en filter kondition på formen
  [[kriterie], kolonnenummer] kun aktive filtre medtages
  ftline[0] er selve filtret
  ftline[1] er kolonnen
  Rutinen kaldes af filterloop som gennemløber hver enkelt kondition i en linie
  Retur er en database der opfylder konditionen
  '''
  dbf=[]
  for line in db:
    for item in ftline[0]:
      #Hvis værdien for den aktuelle kolonne er lige med konditionen medtages linien
      if line[ftline[1]]==item:
        dbf.append(line)
  return dbf

def filterloop(db,krit):
  '''
  For hver kondition i kriterielinien gennemgås denne rutine.
  [[[kriterie], kolonnenummer][[kriterie], kolonnenummer]..] er format for krit
  tomme kriterier pilles ud med reducedfilter
  databasen reduceres for hvert gennemløb 
  Ved slutningen af gennemløb er alle konditioner i i kriterielinien gennemgået 
  Resultat er den endelige database for linien.
  Rutinen kaldes fra dbfilter_beregn for hver kriterielinie samt i 4 tilfælde for actual month, last year month, actual ytd, last year ytd.
  '''
  #Reducere filter til kun at indholde kolonner med aktive konditioner
  ft=reducedfilter(krit)
  antalkrit=len(ft)
  #for hvert kriterie i linien tilpasses databasen
  for i in range(antalkrit):
    db=dbfilter(db,ft[i])
  return db

def dbfilter_beregn(db,krline):
  '''
  input er den rene kriterielinie på formen [[k1],...[k]]
  Beregningsrutine for een kriterielinie.
  filterloop kaldes 4 gange.
  kriteriet rettes tilsvarende. krit[8][0] er år og krit[9][0] er måned
  kriteriet er på formen [[kriterie], kolonnenummer] så [0] er selve kriteriet og [1] er tilsvarende kolonnenummer i database.
  1) Actual month:  måned=actual måned, år = actual år
  2) Actual LY:     måned=actual måned, år = actual år - 1
  3) Actual YTD:    måned=[1,2...actual måned], år = actual år 
  4) Actual LY YTD: måned=[1,2...actual måned], år = actual år-1
  Resultat er 4 databaser
  opsummering af kolonne 10 giver actual volumen og kolonne 11 giver budget.
  '''
  #Actual year
  #Basis kriterie. Starter fra kolonne 3 i kriterietabel hvor kriteriet hentes.
  #Andet led er tilsvarende kolonne. kolonnerækkefølge i kriterie og database er ens.
  krit_mth=[[krline[3+i],0+i] for i in range(10)]
  db_mth=filterloop(db,krit_mth)
  actual=sum([float(line[11]) if line[11] else 0 for line in db_mth])
  #print(actual)

  #Last year
  krit_lyr=copy.deepcopy(krit_mth)
  krit_lyr[8][0]='2018'
  db_lyr=filterloop(db,krit_lyr)
  lastyr=sum([float(line[11]) if line[11] else 0 for line in db_lyr])
  #print(lastyr)

  #ytd actual
  krit_ytd=copy.deepcopy(krit_mth)
  month_actual=krit_ytd[9][0]
  ytd_mth=[str(m) for m in range(1,int(month_actual[0])+1)]
  krit_ytd[9][0]=ytd_mth
  db_ytd=filterloop(db,krit_ytd)
  ytd=sum([float(line[11]) if line[11] else 0 for line in db_ytd])
  #print(ytd)

  #LY ytd
  krit_ly_ytd=copy.deepcopy(krit_ytd)
  krit_ly_ytd[8][0]='2018'
  db_ly_ytd=filterloop(db,krit_ly_ytd)
  ly_ytd=sum([float(line[11]) if line[11] else 0 for line in db_ly_ytd])
  #print(ly_ytd)
  #print(db_mth[0:10])
  actual=sum([float(line[10]) if line[10] else 0 for line in db_mth])
  budget=sum([float(line[11]) if line[11] else 0 for line in db_mth])
  lastyr=sum([float(line[10]) if line[10] else 0 for line in db_lyr])
  ytd=sum([float(line[10]) if line[10] else 0 for line in db_ytd])
  ytd_budget=sum([float(line[11]) if line[11] else 0 for line in db_ytd])
  ly_ytd=sum([float(line[10]) if line[10] else 0 for line in db_ly_ytd])

  print('{:8.1f}{:8.1f}{:8.1f}{:8.1f}{:8.1f}{:8.1f}'.format(actual,budget,lastyr,ytd,ytd_budget,ly_ytd))


#===================HOVEDPROGRAM=============================
db=indlaesdata()
kr=indlaeskriterie()

antallinier=len(kr)

#For hver kriterielinie genereres en resultat.
for i in range(1,antallinier):
  dbfilter_beregn(db,kr[i])






