import pandas as pd
import numpy as np
wine=pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/wine.csv')
#刪除欄位0,3,6,8,11,12,13的資料
wine.drop(wine.columns[[0,3,6,8,11,12,13]],axis='columns',inplace=True)
#命名新欄位
wine.columns=['alcohol', 'hue', 'alcalinity_of_ash', 'magnesium', 'flavanoids', 'proanthocyanins', 'malic_acid']
#設定空值
# 請將第一欄alcohol，索引值1和2的資料改為空值
# 請將第二欄hue，索引值3和4的資料改為空值
wine.iloc[1:3,0]=np.nan
wine.iloc[3:5,1]=np.nan
#將欄位alcohol的空值轉為0
wine.alcohol.fillna(0,inplace=True)
# 將DataFrame中剩餘的空值刪除
wine.dropna(axis='index',how='any',inplace=True)
#請重置index
wine=wine.reset_index(drop=True)
