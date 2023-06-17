import pandas as pd

data=pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/retail.csv')

# 依據欄位Country分組計算欄位Quantity總和
countries=data.groupby('Country').Quantity.sum()
print(countries)

# 由高至低降冪排序，並取得第2名到第10名資料
countries=countries.sort_values(ascending=False)[1:10]
print(countries)

# 繪製長條圖
plot=countries.plot.bar()
