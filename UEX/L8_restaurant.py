import pandas as pd
data=pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/RestaurantVisitors.csv')
data.index=pd.to_datetime(data['date'])

#rest1每周來客數總和
data['week']=data.index.week
total_week_custom=data.groupby('week').rest1.sum()
print(total_week_custom)
print('-'*30)


#假日四間餐廳平均來客數
# print(data[data.holiday==1].loc[:,'rest1':'rest4'].mean())
print(data[(data['holiday']==1)|(data.weekday=='Saturday')|(data.weekday=='Sunday')].loc[:,'rest1':'rest4'].mean())
print('-'*30)


#非假日四間餐廳平均來客數
# print(data[data.holiday!=1].loc[:,'rest1':'rest4'].mean())
print(data[(data.holiday!=1)&(data.weekday!='Saturday')&(data.weekday!='Sunday')].loc[:,'rest1':'rest4'].mean())
