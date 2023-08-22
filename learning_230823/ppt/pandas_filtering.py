import pandas as pd

arrays = [['Fruit', 'Fruit', 'Vegetable', 'Vegetable'], ['Apple', 'Banana', 'Carrot', 'Potato']]
index = pd.MultiIndex.from_arrays(arrays, names=('Category', 'Type'))

# MultiIndex를 사용하여 DataFrame 만들기
df = pd.DataFrame({'Count': [10, 20, 30, 40]}, index=index)
print(df)
print()

# 인덱스로 데이터 선택
selected_data = df.loc['Fruit']
print(selected_data)
