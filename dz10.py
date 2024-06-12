import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

df2 = data.copy()
df2['robot'] = data.replace({'robot': 1,'human': 0})
df3 = df2.copy()
df3['human'] = data.replace({'human': 1,'robot': 0})
print(df3)
