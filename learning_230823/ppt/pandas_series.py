import pandas as pd

# Creating a Series from a list
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s)  # Prints the Series
# a    1
# b    2
# c    3
# d    4
# dtype: int64