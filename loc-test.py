#https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
import pandas as pd
col=["Name","Family","Age","Points"]
indeks=[1,2,3,4,5,6]
data=[["Finn","Holmsø",55,2028],["Vesna","Holmsø",57,1112],["Jens","Jensen",25,1560],["Pia","Flopsen",64,820],["Jenny","Abesen",37,1776],["Gurli","Margrete",21,2213]]
df=pd.DataFrame(data,index=indeks,columns=col)
df1=pd.DataFrame(data,index=indeks,columns=col)

print("")
print("head")
print(df.head(7))

#==========================================================
#iloc anvendes til at finde kolonne eller række ved placering 
#==========================================================
# Single selections using iloc and DataFrame
# Rows:
print("")
print("første række som serie")
print(df.iloc[0]) # first row of data frame - Note a Series data type output.
print("")
print("første række som dataframe")
print(df.iloc[[0]]) # first row of data frame  - Note a DataFrame type output.
print("")
print("anden række som dataframe")
print(df.iloc[[1]]) # second row of data frame 
print("")
print("sidste række som dataframe")
print(df.iloc[[-1]]) # last row of data frame
# Columns:
print("")
print("første kolonne")
print(df.iloc[:,0]) # first column of data frame 
print("")
print("anden kolonne")
print(df.iloc[:,1]) # second column of data frame 
print("")
print("sidste kolonne")
print(df.iloc[:,-1]) # last column of data frame 

print("")
print("3 første rækker og sidste kolonne")
print(df.iloc[0:3,-1])
print("")
print("række 2+3 og sidste kolonne")
print(df.iloc[2:4,-1])
print("")
print("2 første kolonner")
print(df.iloc[:,0:2])
print("")
print("række 2+4 og kolonne 1+3 første kolonner")
print(df.iloc[[1,3],[0,2]])



#==========================================================
#loc anvendes til at finde kolonne eller række med label og index
#==========================================================
print("")
print("Series")
print(df.loc[1]) #Series retur. 1 er index=1
print("")
print("DataFrame")
print(df.loc[[1]]) # med [] kommer en dataframe retur
print("")
print("række og kolonne")
print(df.loc[[1,4],["Name","Age"]])
print("")
print("nyt index")
df.set_index("Family", inplace=True) #Efternavn er index
print(df.head(7))
print("")
print("vælg med nyt index")
print(df.loc[["Holmsø"]]) # Det er index der vælges på
print("")
print("ny data def")
df2=df.loc[["Holmsø"],["Name","Points"]]
print(df2)
print("")
print("boolean serie")
s=[True,False,True,False,True,False]
s1=pd.Series(s,index=indeks)
print(s1)
#Der anvendes en serie med index til at fortælle om den enkelte linie skal medtages eller ej
#Bemærk, at seriens index skal være de samme som listen (df1)
df3=df1.loc[s1]
print(df3)
#df["Age"]<50 skaber en pd.Series per række i df med True and False afhængig af om conditionen er opfyldt
print("")
print("Kondition i kolonne")
df3=df.loc[df["Age"]<50]
print(df3)
print("")
print("Kondition i endswith. Family endswith sen")
#str. for at skelne fra pythoon funktion af samme navn (endswith)
df4=df1.loc[df1['Family'].str.endswith("sen")]
print(df4)
print("")
print("Kondition i contains Name contains en")
#str. for at skelne fra python funktion af samme navn (contains)
df5=df1.loc[df1['Name'].str.contains("en"),["Name","Family"]]
print(df5)
print("")
print("Kondition is in")
df6=df1.loc[df1['Family'].isin(["Holmsø","Flopsen"]),["Name","Family"]]
print(df6)
print("")
print("Kondition AND - &")
df7=df1.loc[df1['Family'].isin(["Holmsø","Flopsen"]) & (df1["Age"]>60),["Name","Family"]]
print(df7)
print("")
print("Kondition OR |")
df8=df1.loc[(df1["Age"]>50) | (df1["Age"]<30),["Name","Family","Age"]]
print(df8)
print("")
print("Kondition NOT ~ alder>40")
df8=df1.loc[~(df1["Age"]>40),["Name","Family","Age"]]
print(df8)
print("")
print("Kondition Apply function-fornavne med 4 bogstaver")
df9=df1.loc[df1["Name"].apply(lambda x: len(x))==4]
print(df9)
print("")
print("Ændre data med kondition. Alle med sen efternavn får 3000 points")
df1.loc[df1['Family'].str.contains("sen"), "Points"] = 3000
print(df1)
