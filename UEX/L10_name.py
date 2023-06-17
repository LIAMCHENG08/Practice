import pandas as pd
names=pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/US_Baby_Names_Lite.csv')
#找出名字是emma的資料
search_emma=names[names['Name']=='Emma']
print(search_emma)

#找出名字是An開頭且為女性資料
mask1=names['Name'].str.startswith('An')
mask2=names['Gender']=='F'
an_f=names[mask1 & mask2]
print(an_f)

#找出2004年 最多女性菜市場名
names[(names['Year']==2004) & (names['Gender']=='F')].groupby('Name').Count.sum().sort_values(ascending=False).head()

