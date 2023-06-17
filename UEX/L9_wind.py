import pandas as pd
import datetime as dt

data_url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data'
#sep用正則 parse_dates把前三欄合併變時間
data = pd.read_csv(data_url, sep = '\s+', parse_dates = [[0, 1, 2]])

def fix(x):
    year=x.year -100 if x.year > 2060 else x.year
    return dt.datetime(year,x.month,x.day)
data['Yr_Mo_Dy']=data['Yr_Mo_Dy'].apply(fix)

data.index=pd.to_datetime(data['Yr_Mo_Dy'])

data_describe=data.describe()
# print(data_describe)

day_stats=pd.DataFrame()
day_stats['min']=data.min(axis=1)
day_stats['max']=data.max(axis=1)
day_stats['mean']=data.mean(axis=1)
day_stats['std']=data.std(axis=1)
print(day_stats)
#取得一月份平均
# data.loc[data.index.month==1].mean()

data.groupby(data.index.to_period('M')).mean()

monthly=data.groupby(data.index.to_period('M')).agg(['mean','min','max'])

monthly.loc[monthly.index[0:12],'RPT':'KIL']
#%%
import pandas as pd
import datetime as dt

data_url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data'
#sep用正則 parse_dates把前三欄合併變時間
data = pd.read_csv(data_url, sep = '\s+', parse_dates = [[0, 1, 2]])

def fix(x):
    year=x.year -100 if x.year > 2060 else x.year
    return dt.datetime(year,x.month,x.day)
data['Yr_Mo_Dy']=data['Yr_Mo_Dy'].apply(fix)

data.index=data['Yr_Mo_Dy']

#各地區每年每周的平均風速
weekly=data.groupby(data.index.to_period('W')).mean()
print(weekly)

#每個地區每個月的風速平均、最小值和最大值
monthly=data.groupby(data.index.month).agg(['mean','min','max'])
print(monthly)