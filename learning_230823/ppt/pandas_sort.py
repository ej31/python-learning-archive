import pandas as pd

# Creating a DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [30, 25, 22]
})

# Sorting by Age
df_sorted = df.sort_values('Name')
print(df_sorted)

df_sorted = df.sort_index()
print(df_sorted)
