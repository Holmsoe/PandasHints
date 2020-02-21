import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
#Brug denne og ikke pylab

def ex1():
    x=np.linspace(0,1,10)
    plt.plot(x,x*x,label="x i anden")

def ex2():  
    fig = plt.figure() # an empty figure with no axes
    fig, ax_lst = plt.subplots(2, 2) # a figure with a 2x2 grid of Axes

def ex3():
    x = np.arange(0, 10, 0.2)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    
    #show er mest nødvendig i gamle versioner
    #plt.show()
    

def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph
    Parameters
    ----------
    ax : Axes
    The axes to draw to
    data1 : array
    The x data
    data2 : array
    The y data
    param_dict : dict
    Dictionary of kwargs to pass to ax.plot
    Returns
    -------
    out : list
    list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out
    # which you would then use as:
    
def ex4():
    x=np.linspace(0,np.pi,20)
    y=np.sin(x)
    
    fig, ax = plt.subplots(1, 1) 
    my_plotter(ax, x,y, {'marker': 'x'})


def ex5():    
    x=np.linspace(0,np.pi,20)
    y=np.sin(x)
    y1=np.cos(x)   
   
    fig, (ax1, ax2) = plt.subplots(1, 2)
    my_plotter(ax1, x, y, {'marker': 'x'})
    my_plotter(ax2, x, y1, {'marker': 'o'})

def ex6():
    x=np.linspace(0,np.pi,20)
    y=np.sin(x)
    ax = plt.gca()
    ax.plot(x,y)
    plt.ylabel('y akse')
    plt.ylabel('x akse')
    
def ex7():
    plt.ion()
    plt.plot([1.6, 2.7])  

def ex8():
    plt.ion()
    mplstyle.use(['dark_background', 'ggplot', 'fast'])
    #Style beholdes når den er sat
    plt.plot([1.6, 2.7])

def ex9():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    plt.axis([0, 6, 0, 20])
    
def ex10():
    t = np.arange(0., 5., 0.2)
    # red dashes, blue squares and green triangles
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

def ex11():
    data = {'a': np.arange(50),
    'c': np.random.randint(0, 50, 50),
    'd': np.random.randn(50)}
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100
    plt.scatter('a', 'b', c='c', s='d', data=data)
    plt.xlabel('entry a')
    plt.ylabel('entry b')
    
def ex12():
    names = ['group_a', 'group_b', 'group_c']
    values = [1, 10, 100]
    plt.figure(figsize=(9, 3))
    plt.subplot(131)
    plt.bar(names, values)
    plt.subplot(132)
    plt.scatter(names, values)
    plt.subplot(133)
    plt.plot(names, values)
    plt.suptitle('Categorical Plotting')
    
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
    
    
def ex13():
    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)
    plt.figure()
    plt.subplot(211)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
    plt.subplot(212)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
    
def ex14():
    # Make a data frame
    df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21), 'y4': np.random.randn(10)+range(6,16), 'y5': np.random.randn(10)+range(4,14), 'y6': np.random.randn(10)+range(2,12), 'y7': np.random.randn(10)+range(5,15), 'y8': np.random.randn(10)+range(4,14) })
     
    # All the possibility of style:
    possibilities = [u'seaborn-darkgrid', u'seaborn-notebook', u'classic', u'seaborn-ticks', u'grayscale', u'bmh', u'seaborn-talk', u'dark_background', u'ggplot', u'fivethirtyeight', u'_classic_test', u'seaborn-colorblind', u'seaborn-deep', u'seaborn-whitegrid', u'seaborn-bright', u'seaborn-poster', u'seaborn-muted', u'seaborn-paper', u'seaborn-white', u'seaborn-pastel', u'seaborn-dark', u'seaborn', u'seaborn-dark-palette']
     
    # Initialise figure
    my_dpi=96
    plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)
     
    # Let's do a chart per possibility:
    for n, v in enumerate(possibilities):
        print(n, v)
     
        # I set the new style
        plt.style.use(v)
         
        # Start new place in the figure
        plt.subplot(5 ,5, n + 1)
         
        # multiple line plot
        for column in df.drop('x', axis=1):
            plt.plot(df['x'], df[column], marker='', color='grey', linewidth=1, alpha=0.4)
         
        # And highlith one
        plt.plot(df['x'], df['y5'], marker='', color='orange', linewidth=4)
         
        # Add a title to say which style it is
        plt.title(v, fontsize=10, fontweight=0, color='grey', loc='left')
         
        # remove labels
        plt.tick_params(labelbottom=False)
        plt.tick_params(labelleft=False)
    
    #plt.show()
     
    # save
    #plt.savefig('PNG/#199_Matplotlib_style_sheet.png', dpi=96, bbox_inches='tight')

plt.style.use('classic')
ex12()

