"""
Index를 설명합니다.
"""
import pandas as pd

# Creating an Index
index = pd.Index([1, 2, 3, 4], name='Numbers')

# Creating a Series with the Index
s = pd.Series([10, 20, 30, 40], index=index)

# Output the Series
print(s)
# Numbers
# 1    10
# 2    20
# 3    30
# 4    40
# dtype: int64

# Accessing the Index
print(s.index)
# Int64Index([1, 2, 3, 4], dtype='int64', name='Numbers')
