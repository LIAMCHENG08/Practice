import pandas as pd

data=pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/titanic.csv')
# 鐵達尼號乘客男性、女性數量
male_1=data[data.Sex=='male'].Sex.count()
female_1=data[data['Sex']=='female'].Sex.count()

#圓餅圖
data1={'sex':[male_1,female_1]}
df1=pd.DataFrame(data1,index=['male','female'])
plot=df1.plot.pie(y='sex',figsize=(5,5))

# 鐵達尼號倖存乘客男性、女性數量
male_2=data[(data['Sex']=='male') & (data['Survived']==1)].Sex.count()
female_2=data[(data['Sex']=='female') & (data['Survived']==1)].Sex.count()

#圓餅圖
data2={'sex':[male_2,female_2]}
df2=pd.DataFrame(data2,index=['male','female'])
plot=df2.plot.pie(y='sex',figsize=(5,5))