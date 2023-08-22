import pandas as pd

df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'A': [3, 4]})

concatenated = pd.concat([df1, df2])
print(concatenated)
