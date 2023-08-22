import pandas as pd

df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})

merged = pd.merge(df1, df2, on='key')
print(merged)

# Outer Join
merged_outer = pd.merge(df1, df2, on='key', how='outer')
print(merged_outer)

# Inner Join
merged_inner = pd.merge(df1, df2, on='key', how='inner')
print(merged_inner)

# Outer Join
merged_left = pd.merge(df1, df2, on='key', how='left')
print(merged_left)

# Right Join
merged_right = pd.merge(df1, df2, on='key', how='right')
print(merged_right)

# join()
df1 = pd.DataFrame({'A': [1, 2]}, index=['x', 'y'])
df2 = pd.DataFrame({'B': [3, 4]}, index=['x', 'y'])

joined = df1.join(df2)
print(joined)
