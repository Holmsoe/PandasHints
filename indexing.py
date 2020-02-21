import pandas as pd

def ReadDatabase(db_name):
    db=[]
    with open(db_name) as f:
        for line in f:
            line=line.strip('\t\n')
            db.append(line.split('\t'))
    return db

db_name="FaxePandas.txt"
db=ReadDatabase(db_name)
col_names=["nature", "dist", "country", "customer", "shipto", "material", "process", "mduse", "year", "month", "actual", "budget"]
db_pd=pd.DataFrame(db,columns=col_names)
db_pd[["customer","shipto","material","year","month","actual","budget"]] = db_pd[["customer","shipto","material","year","month","actual","budget"]].apply(pd.to_numeric, errors='coerce')
db_pd=db_pd.fillna(0)

print(db_pd.head(5))


#Simpel slicing
#Flere kolonner med liste
print(db_pd[["year","month","material","actual"]].head(5))
#En kolonne med dot
print(db_pd.actual.head(5))
#Rækker med index-5 første
print(db_pd[:5])
#Rækker med index- hver tolvte fra 10 til 300
print(db_pd[10:300:12].head(5))
#Rækker med index-undtagen de sidste 100
print(db_pd[:-100].tail(5))
#Rækker bagfra-step -1
print(db_pd[::-1].head(5))

#loc
# format af loc db[rækkeindex,søjle] eller db[rækkeindex][søjle) - både række og søjle er en liste
#Så hvis kun en liste er det søjle
print(db_pd.loc[:5,["year","month","material","actual"]].head(5))


#Nyt index. nature
db_pd=db_pd.set_index(["nature"])
#Med række index
print(db_pd.head(5))
print(db_pd.loc["U"].head(5))
print(db_pd.loc["U",["year","month","material","actual"]].head(5))

db_pd=db_pd.reset_index()

#Betingelser
#Betingelser vælge rækker. : siger at alle søjler skal med
print(db_pd.loc[db_pd["month"]==5,:].head(5))
print(db_pd.loc[db_pd["month"]==5].head(5)) #underforstået at alle søjler skal med

#Iloc
print(db_pd.iloc[10:15])
print(db_pd.iloc[[1,5,10,15]])
print(db_pd.iloc[[i for i in range(1,100) if i%7==0]])

# Multindex

db_pd=db_pd.set_index(["material","mduse"])
print(db_pd.head(50))
print(db_pd.index.get_level_values(0))
print(db_pd.index.get_level_values(1))

mat=db_pd.index.get_level_values(0)
    
for item in set(mat): print(item)

#Valg at index 0-material
print(db_pd.loc[87].head(5))
#Valg at index 1-mduse
print(db_pd.loc[[92,96]].head(5))
#2 level valg
print(db_pd.loc[[(92,"AAZ"),(96,"DAG")]].head(5))

#Reset multindex
#OBS hvis en kolonne er index kan den ikke anvendes i loc.

db_pd=db_pd.reset_index()
print(db_pd.head(5))
mat87=db_pd["material"]==87
mat96=db_pd["material"]==96
    
db_test=db_pd.loc[mat87 | mat96]
print(db_test.iloc[700:800].head(50))
print(db_test.loc[mat96].head(50))

# Er falsk da kun nogle i db_pd har materiale 87
#mat87 er et boolean liste for materialekolonne der fortæller om materialenummer=87
print(mat87.all())

# Er True
print(mat87.any())