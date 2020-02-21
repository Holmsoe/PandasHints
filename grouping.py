import pandas as pd

db_ind=[]
with open("FaxePandas.txt") as f:
    for line in f: 
        line=line.strip('\t\n')
        line=line.split('\t')
        db_ind.append(line)

col_names=["nature", "dist", "country", "customer", "shipto", "material", "process", "mduse", "year", "month", "actual", "budget"] 
db=pd.DataFrame(db_ind,columns=col_names)
db[["customer","shipto","material","year","month","actual","budget"]] = db[["customer","shipto","material","year","month","actual","budget"]].apply(pd.to_numeric, errors='coerce')
db=db.fillna(0)
print(db["material"].head())

#printer en kolonne i database
#for a in db:
#    if a=="nature": print(db[a])

#Gruppere per materiale
mat_group=db.groupby("material")

#Printer linier per gruppe

print(type(mat_group))
print("\n")


#=========groups
#groups laver et dictionary med alle materialenavne og deres placeringer
#Længden er antal elementer
group_dict=mat_group.groups

#Dictionary for materiale=87
print(group_dict[87])
#Længde af dictionary=antal linier med materiale 87
print(len(group_dict[87]))

#Materiale og antal per materiale
for key in group_dict.keys():
    print('{:4d}{:4d}'.format(key,len(group_dict[key])))
print("\n")
  
#=========size
#Laver samme liste med navn og størrelse
mat_size=mat_group.size()
#Bemærk formattering er OK når det er en pandas type
print("resultat af .size(). bemærk sorteret efter index")
print(mat_size.head())
print("\n")

#mat_size er Series
print("resultatet er en pandas serie")
print(type(mat_size))
print("\n")

print("Sotere efter størrelse")
print(mat_size.sort_values(ascending=False).head())
print("\n")

print("sortere efter index")
print(mat_size.sort_index().head())
print("\n")


#===========flere groups og size
#groupby anvender normalt kolone men kan også anvende index
mat_md=db.groupby(["material","mduse"])
print("Groupby 2 grupper")
print(mat_md.size().head())
print("\n")

#soreterer efter størrelse
print("Sorteret efter value")
print(mat_md.size().sort_values(ascending=False).head())
print("\n")

#level=1 giver andet index
print("Sorteret efter index. Angivet med level hvis flere")
print(mat_md.size().sort_index(level=1).head())
print("\n")

#================Grouby med flere level index
db_3level=db.set_index(["nature","dist","mduse"])
print("3 index level db")
print(db_3level.head())
print("\n")
print("groupby per level - her md use og dist")
group_index=db_3level.groupby(level=["mduse","dist"])
print(group_index.size().head(10))
print("\n")

#=================SUM
print("Sum - actual - af en gruppe")
print(mat_group["actual"].sum().head())
print("\n")

print("Samme sum uden group, men over et index. Her er materialer ikke sorteret")
db_index=db.set_index(["material","mduse"])
print(db_index["actual"].sum(level="material").head())
print("\n")

print("Sum i 2 niveauer med index uden gruppe")
print(db_index["actual"].sum(level=["material","mduse"]).head())
print("\n")

mat_dist=db.groupby(["dist","material"])
print("Sum - actual - per gruppe")
print(mat_dist["actual"].sum().head())
print("\n")