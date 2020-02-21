import pandas as pd

def htmltext():
    '''
    Hente fil fra net og gemme
    '''
    import requests
    url="https://www.wikipedia.org/"
    r=requests.get(url)
    text=r.text
    
    print(text)
    
def txtfromweb1():
    '''
    Text, herunder csv fra net og overførsel til pandas
    '''
    #dette henter og opretter fil med urllib.request 
    # Bemærk, at urllib og urllib2 ikke anbefales da de udgår på et tidspunkt

    import urllib.request
    #Se: https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/
    url="https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
    
    #Dette henter filen som bytes
    response = urllib.request.urlopen(url)
    data = response.read()      # a `bytes` object
    #Lave om til text format
    text = data.decode('utf-8')
    
    return text

def txtfromweb2():
    '''
    Text, herunder csv fra net og overførsel til pandas
    '''
    #dette henter og opretter fil med requests

    import requests
    #Se: https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/
    url="https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
    
    #Her skal ikke konverteres fra bytes
    response=requests.get(url)
    text = response.text      # a `bytes` object
    
    return text

def tilpasfil(filtext):
    
    # Tilpasning er individuel for hver fil
    #Split på linier
    df=filtext.split("\n")
    #Split på komma som omkranser teksten
    df1=[]
    for txt in df:
        df1.append(txt.split(","))
    #Split på semikolon for hver enkelt element
    df2=[]    
    for line in df1:
        df2.append(line[0].split(";"))
        
    #Overførsel til Pandas       
    df_pd=pd.DataFrame(df2)
    
    #Change header to first line
    new_header = df_pd.iloc[0] 
    df_pd = df_pd[1:]
    df_pd.columns = new_header 
    
    #Vis headers
    for kolonne in df_pd.columns:
        print(kolonne)
        
    print(df_pd.head())
    
    
udfraweb=txtfromweb2()
tilpasfil(udfraweb)