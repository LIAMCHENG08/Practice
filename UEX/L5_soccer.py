import pandas as pd

data=pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/Euro_2012_stats_TEAM.csv',
                 sep=',')

#dataframe['欄位名稱'] 如果要取兩個欄位以上要多加[]dataframe[['欄位名稱','欄位名稱']] 
cards=data[['Team','Yellow Cards','Red Cards']]
print(cards)
#降冪
cards.sort_values('Yellow Cards',ascending=(False))

#series 
print(data.Goals) # =data['Goals']
#平均分數
print(data.Goals.mean())
#round 四捨五入
print(round(data.Goals.mean()))

#過濾條件
print(data.Goals>5)
#尋找球隊得分>5分
print(data[data.Goals>5])
#尋找球隊名稱是s國家
print(data[data.Team.str.startswith('S')])
#ex
print(data.Team.iloc[3:7])
