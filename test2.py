#https://www.tutorialspoint.com/python_pandas/python_pandas_quick_guide.htm

import pandas as pd
from random import randint

#Create a series with 100 random numbers
s = pd.Series([randint(0, 9) for i in range(10)], index=[str(i)+"a" for i in range(10)])

print("Series")
print("="*30)

print(s)

print("")
print("axes")
print("="*10)
print(s.axes)

print("")
print("empty?")
print("="*10)
print(s.empty)