import pandas as pd

#就業資料
data=pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/u.user.txt',
                  sep='|',index_col=('user_id'))

#GROUPBY
ocupy_avg_age=data.groupby('occupation').age.mean()

#將性別轉換為數值
def gender_to_numeric(x):
    if x=='M':
        return 1
    elif x=='F':
        return 0

gender_n=data['gender'].apply(gender_to_numeric)
data['gender_n']=gender_n

#計算每個職業男生占比
#每個職業男性數量總和/每個職業總數
result=data.groupby('occupation').gender_n.sum()/data.occupation.value_counts()*100
result=result.sort_values(ascending=False)

print(result)

#GROUPBY agg聚合
# ocupy_age=data.groupby('occupation').age.agg(['max','min','mean','count'])

ocupy_gender=data.groupby(['occupation','gender']).agg({'age':'mean','gender':'count'})

print(ocupy_gender)
