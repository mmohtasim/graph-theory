import pandas as pd
from scipy.stats import entropy

# data = [True,False,True,True,True,False,False,True,False,False,True,True,False]
data = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0 ]

pd_series = pd.Series(data)

counts = pd_series.value_counts()

entropy = entropy(counts)

print(entropy)