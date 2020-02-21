import pandas as pd
data1 = {
        'subject_id': ['1', '2', '3', '4', '5','7'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung','Finn'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches','Holmsø']}
df1 = pd.DataFrame(data1, columns = ['subject_id', 'first_name', 'last_name'])

data2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
df2 = pd.DataFrame(data2, columns = ['subject_id', 'first_name', 'last_name'])

data3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
df3 = pd.DataFrame(data3, columns = ['subject_id','test_id'])

print(df1)
print("")
print(df2)
print("")
print(df3)

#================================
#concatenation
#================================

#I python kombinerer vi tekst i een kolonne
#===============================

#kombinere to tekst kolonner i ny  kolonne
#Bemærk per index. kombinering stopper med korteste DataFrame
dfplus = df1['first_name'] + " " + df2['first_name']
print("to tekstkolonner fra 2 dataframes")
print(dfplus)
print("")

#kombinere to tekst kolonner i ny  kolonne.Fra samme DataFrame
dfplus2 = df1['first_name'] + " " + df1['last_name']
print("to tekstkolonner fra samme dataframe")
print(dfplus2)
print("")

#kombinere to tekst kolonner i ny  kolonne.Fra samme DataFrame
dfplus4 = df1['first_name'] + " " + df1['subject_id']
print("tekstkolonne og talkolonne fra samme dataframe")
print(dfplus4)
print("")


#kombinere tekst of tal kolonne
dfplus1 = df1['first_name'] + " "+ df2['subject_id']
print("tekstkolonne og talkolonne fra 2 dataframes")
print(dfplus1)
print("")

#kombinere i ny kolonne
dfkomb=dfplus+" " + dfplus1
print("kombinere to kombinerede ")
print(dfkomb)
print("")

#Gange en serie med 2
def gange(ind):
    return ind*2

testserie=pd.Series([10,20,30,40])
print("test serie")
print(testserie)
print("test serie ganget med 2")
print(testserie.map(gange))


Dates = {'Day': [1,2,3,4,5], 
        'Month': ['Jun','Jul','Aug','Sep','Oct'], 
        'Year': [2016,2017,2018,2019,2020]} 
datobase = pd.DataFrame(Dates, columns= ['Day', 'Month','Year']) 
print("")
print("database med datoer i kolonner")
print (datobase)
#pd.Series.map kan ændre en serie
concatdato = datobase['Day'].map(str) + '-' +datobase['Month'].map(str) + '-' + datobase['Year'].map(str)
print("")
print("database med datoer i kombineret")
print (concatdato)
print("\n")

#I pandas komberes database i søjler
df_concat = pd.concat([df1, df2])
print("Concat vandret kombinere med axis=0 eller uden axis")
print(df_concat)
print("\n")

df_concat1 = pd.concat([df1, df2],axis=1)
print("Concat lodret kombinere med axis=1")
print(df_concat1)
print("\n")

df1a=df1.set_index("subject_id")
df2a=df2.set_index("subject_id")

df_concat1a = pd.concat([df1a, df2a],axis=1,sort=True)
print("Concat med index")
print(df_concat1a)
print("\n")

df_append=df1.append(df2,ignore_index=True)
print("append er det samme som concat med axis=0. ignore_index = True giver nye index med tal og gamle index fjernes")
print(df_append)

df_appenda=df1a.append(df2a,ignore_index=False)
print("append er det samme som concat med axis=0. ignore index = False bibeholder index")
print(df_appenda)
