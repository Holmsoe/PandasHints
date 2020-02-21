#https://www.tutorialspoint.com/python_pandas/python_pandas_quick_guide.htm


import pandas as pd

l1=[i*i for i in range(6)]
l2=[1/i for i in range(1,7)]
d1=data = {'a' : 0., 'b' : 1., 'c' : 2.}
a1=[[5+i+j for i in range(6)] for j in range(6)]


s1= pd.Series(l1)
s2= pd.Series(l2)
print(s1)

print(s2)
print('{:<5.2f}{:<5.2f}{:<5.2f}{:<5.2f}{:<5.2f}{:<5.2f}'.format(*s2))
for line in s2:
    print('{:<5.2f}'.format(line),end="")
    
s3=pd.Series(d1)
print("")
print(s3)

s4=pd.Series(a1)
print(s4)

s5 = pd.Series(5, index=[i for i in range(6)])
#s5 = pd.Series(5, index=[0, 1, 2, 3,4,5])
print(s5)

s6 = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s6)
print("")
print("hente med index",s6['a'])
print("hente med position",s6[0])
print("")
print("første 3 elementer")
print(s6[:3])
print("sidste 3 elementer")
print(s6[-3:])
print("flere index number")
print(s6[["a","c"]])    #Bemærk argument er en liste

l3=(1,2,5,6,8)
print("tuple",l3)

t1=pd.DataFrame(a1)
print(t1)

#Hver linie separat
print("")
print("input i separate linier")
a2=[["Finn",1960,30000],["Gurli",1972,25000],["Svend",1953,40000],["Pia",1968,35000]]
t2=pd.DataFrame(a2,columns=["Navn","År","Løn"],index=[1,2,3,4])
print(t2)

#Hver søjle separat
print("")
print("input i separate søjler")
data = {'Navn':['Finn', 'Gurli', 'Svend', 'Pia'],'År':[1960,1972,1953,1968],"Løn":[30000,25000,40000,35000]}
df = pd.DataFrame(data)
print(df)

#Variable. Alle lister skal have samme længde
print("")
print("input i variable lister")
navne=['Finn', 'Gurli', 'Svend', 'Pia']
born=[1960,1972,1953,1968]
lon=[30000,25000,40000,35000]
indeks=['a','b','c','d']

data = {'Navn':navne,'År':born,"Løn":lon}
df = pd.DataFrame(data,index=indeks)
print(df)

print("")
print("liste af dictionaries-tomme felter mulige")
ind=[{"Navn":"Finn","År":1960,"Løn":30000},{"Navn":"Gurli","År":1972},{"Navn":"Svend","År":1953,"Løn":40000},{"Navn":"Pia","År":1968,"Løn":35000}]
indeks=['a','b','c','d']
df=pd.DataFrame(ind,index=indeks)
print(df)

print("")
print("liste af dictionaries-definerede kolonnenavne")
#Bemærk, at kolonner der er defineret i dictionary men ikke i kolonneoversigt udelades. 
#Hvis der mangler data fra overskriftliste indsættes NaN
ind=[{"Navn":"Finn","År":1960,"Løn":30000},{"Navn":"Gurli","År":1972},{"Navn":"Svend","År":1953,"Løn":40000},{"Navn":"Pia","År":1968,"Løn":35000}]
indeks=['a','b','c','d']
kolonner=["Navn","Efternavn","År"]
df=pd.DataFrame(ind,index=indeks,columns=kolonner)
print(df)

print("")
print("liste af pd.Series")
#En serie er en kolonne. lister merges på basis af index. Manglende index -> NaN
d = {'one' : pd.Series([1, 2, 3,53], index=['a', 'b', 'c','q']),
   'two' : pd.Series([5, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)


print("")
print("hente kolonne med navn")
a2=[["Finn",1960,30000],["Gurli",1972,25000],["Svend",1953,40000],["Pia",1968,35000]]
df=pd.DataFrame(a2,columns=["Navn","År","Løn"],index=[1,2,3,4])
print(df["Navn"])

print("")
print("appending column with pd.Series")
a2=[["Finn",1960,30000],["Gurli",1972,25000],["Svend",1953,40000],["Pia",1968,35000]]
df=pd.DataFrame(a2,columns=["Navn","År","Løn"],index=[1,2,3,4])
ny=pd.Series([50,40,55,45],index=[1,2,3,4])
df["Trækpct"]=ny
print(df)

print("")
print("gange 2 kolonner")
df["Skat"]=df["Løn"]*df["Trækpct"]/100
print(df)

print("")
print("slette kolonne")
#Bemærk at tallene i "Skat" kolonne ikke er afhængig af "Løn" når de en gang for alle er beregnet. 
del df["Løn"]
#df.pop("Løn")
print(df)

print("")
print("vælg kolonne på overskrift")
print(df["Skat"])

print(df)

print("")
print("vælg række på index")
print("med iloc- nummer i rækken")
print(df.iloc[2])
print("med slice")
print(df[1:2])

print("")
print("append row")
a2=[["Finn",1960,30000],["Gurli",1972,25000],["Svend",1953,40000],["Pia",1968,35000]]
df=pd.DataFrame(a2,columns=["Navn","År","Løn"])
a3=[["FinnA",1961,31000],["Gunnar",1948,21000]]
df1=pd.DataFrame(a3,columns=["Navn","År","Løn"])
dfny=df.append(df1)
print(dfny)
print("")
print("slet række med index")
dfny = df.drop(0)
print(dfny)