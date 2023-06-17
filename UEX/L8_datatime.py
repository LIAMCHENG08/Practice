import datetime as dt
day=dt.datetime(year=2020,month=5,day=30,hour=9,minute=4,second=30)

today=dt.datetime.today()
print(today.year)
print(today.month)
print(today.day)
print(today.hour)

#strftime %Y %m %d %H %M %S
datestr=today.strftime('%Y/%m/%d %H:%M:%S')

#TYPE確認
print(type(today))
print(type(datestr))

#調整時間timedelta
delta=dt.timedelta(days=1)
print(today+delta)
#%%
import pandas as pd
import pandas_datareader.data as data
import datetime as dt

df = data.DataReader('AAPL', data_source = 'stooq', start='2022-10-01',end='2022-12-31')
print(df)
#週數
print(df.index.week)
df['week']=df.index.week
df.groupby('week').Volume.sum()
ten=df.resample('10D').mean()
