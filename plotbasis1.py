import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def fig_grid1():
    #Vi kan håndtere flere plots. De befinder sig i figurer.
    #Basic
    fig = plt.figure()
    fig.add_subplot(111)
    
    fig = plt.figure(2) # hvis ikke tl nummereres figurer forløbende
    fig.add_subplot(111) 
    
    #Her er en figur med 4 plots i grid
    fig = plt.figure()
    fig.add_subplot(221)   #top left
    fig.add_subplot(222)   #top right
    fig.add_subplot(223)   #bottom left
    fig.add_subplot(224)   #bottom right
    
    fig2 = plt.figure()
    fig2.add_subplot(221)   #top left
    fig2.add_subplot(222)   #top right
    fig2.add_subplot(212)   #bottom
    #Denne betyder anden række har en kolonne og fig placeres til højre 

#Alternativ til de uoverskuelige nummerering ovenfor    
def fig_grid2():
    #fig = plt.subplot()
    fig = plt.figure()
    grid = plt.GridSpec(2, 2, wspace=0.4, hspace=0.3)
    
    a=plt.subplot(grid[0,0:])
    b=plt.subplot(grid[1, 0])
    c=plt.subplot(grid[1, 1])
    
    x=[i for i in range(10)]
    y=[i*i for i in range(10)]
    a.plot(x,y,label="min label")
    a.legend()
    
    a.set_title("to kolonner")
  
def fig_ax():
    '''
    plt.subplots() is a function that returns a tuple containing a figure and axes object(s). 
    Thus when using fig, ax = plt.subplots() you unpack this tuple into the variables fig and ax. 
    Having fig is useful if you want to change figure-level attributes or save the figure as an image file later 
    (e.g. with fig.savefig('yourfilename.png')). 
    You certainly don't have to use the returned figure object but many people do use it later so it's common to see. 
    Also, all axes objects (the objects that have plotting methods), have a parent figure object anyway, thus:

    fig, ax = plt.subplots()
    is more concise than this:

    fig = plt.figure()
    ax = fig.add_subplot(111)
    '''
    f, ax = plt.subplots() #to variable sættes: fig og ax
    ax.set_title('Simple plot')
    
def fig_ax2():
    fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
    ax[1,1].text(0.5, 0.5, "min tekst",
                      fontsize=18, ha='center')    

def fig_ax3():
    fig, ax = plt.subplots(2,1)
    ax[0,0].text(0.5,0.5,"0,0")
    ax[0,1].text(0.5,0.5,"0,1")
    ax[1,0].text(0.5,0.5,"1,0",ha='center')
    ax[1,1].text(0.5,0.5,"1,1",ha='center')
 
def fig_ax4():
    
    fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
    ax[0].set_title("Sinuskurve")
    ax[1].set_title("Cosinuskurve")
    ax[0].set_xlim(-np.pi,np.pi)
    
    #Bemærk at formatet  ax[0] kun virker med en dimensionalt array ellers anvendes ax[0,0]
    
    #Bemærk, at vi kun har sat xlimit for een figur. 
    #Hvis vi bruger sharex=True bliver den anden automatisk sat til samme limit. 

    
    #Justering af afstand og størrelse.
    '''
    defaults
    left  = 0.125  # the left side of the subplots of the figure
    right = 0.9    # the right side of the subplots of the figure
    bottom = 0.1   # the bottom of the subplots of the figure
    top = 0.9      # the top of the subplots of the figure
    wspace = 0.2   # the amount of width reserved for blank space between subplots,
                   # expressed as a fraction of the average axis width
    hspace = 0.2   # the amount of height reserved for white space between subplots,
                   # expressed as a fraction of the average axis height
    
    denne justering virker ikke sammen med tight_layout
    '''
    #plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
    
    plt.tight_layout()    # undgår mærkelige overlap
    x=np.linspace(-np.pi,np.pi,50,endpoint=True)
    y1=np.sin(x)
    y2=np.cos(x)   
    
    gsin=np.array([x,y1]).T   #transponere for at få kolonner 
    gcos=np.array([x,y2]).T   #transponere for at få kolonner
    
    print(gsin[:,0])
    
    #Her plotter vi direkte fra lister 
    ax[0].plot(gsin[:,0],gsin[:,1])
    ax[1].plot(gsin[:,0],gcos[:,1])
    
    
    
    #Her plotter vi fra Pandas dataframe
    #graf1=pd.DataFrame(gsin,columns=["x","sin"])
    #graf2=pd.DataFrame(gcos,columns=["x","cos"])
    #Bemærk, at paramtre kan sættes direkte
    #g1=graf2.plot(x='x',y='cos',legend=False,ax=ax[1],xlim=(-np.pi,np.pi))
    #g1.set_xlim(-np.pi,np.pi)


def fig_ax5():
    fig = plt.figure()
    #Placering med koordinater
    ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4],xticklabels=[], ylim=(-1.2, 1.2))
    ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4],ylim=(-1.2, 1.2))

    x = np.linspace(0, 10)
    ax1.plot(np.sin(x))
    ax2.plot(np.cos(x));


    

    
fig_grid2()
