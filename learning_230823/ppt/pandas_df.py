"""
데이터 프레임을 볼 수 있습니다.
"""
import pandas as pd

# Creating a DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

# Output the DataFrame
print(df)
#        Name  Age         City
# 0     Alice   25     New York
# 1       Bob   30  Los Angeles
# 2   Charlie   22      Chicago
