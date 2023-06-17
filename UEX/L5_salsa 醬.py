import pandas as pd

data=pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/chipotle.tsv',
                 sep='\t')

#將item_price 從字串變float
# for value in data.item_price:
#     print(value[1:])

price=[float(value[1:]) for value in data.item_price]
data['item_price']=price
# 計算item price 四捨五入
print(round(data.item_price.mean()))
# item price 價格大於7的資料
mask=data['item_price']>7
print(data[mask])
# item price 價格大於7且choice_description欄位含Fresh Tomato Salsa的資料
mask2=data['choice_description'].str.contains('Fresh Tomato Salsa')
print(data[mask & mask2])
# item price 最貴一筆的資料
print(data.sort_values('item_price',ascending=(False)).head(1))
# 切第3列到10列 欄位 order id 到 item name
print(data.iloc[3:11,0:3])
