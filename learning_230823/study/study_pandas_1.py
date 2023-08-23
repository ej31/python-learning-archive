import pandas as pd

_pd_series_demo = pd.Series([99, 100.2, 101.3, 102.4], index=[0, 1, 2, 3])
# print(_pd_series_demo)

_pd_dataframe_demo = pd.DataFrame({
    "Name": ["홍길동", "김갑수", "John Doe", "John Wick"],
    "Age": ["30", "40", "50", "60"],
    "Height": [184, 194, 204, 214]
})

# print(_pd_dataframe_demo)
# print(_pd_dataframe_demo.index)

_pd_idx = pd.Index([5, 6, 7, 8], name="AWS Index")
_pd_series_2 = pd.Series(
    ["Kim", "Lee", "Park", "Choi"], index=_pd_idx
)
print(_pd_series_2)
print(_pd_series_2.index)


