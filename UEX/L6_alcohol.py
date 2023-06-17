import pandas as pd

data=pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/drinks.csv',
                 sep=',',index_col='country')

#全世界平均消費啤酒(beer)的數量是多少
print(data.iloc[:,1].mean())
#每個洲平均消費啤酒(beer)的數量是多少
avg_beer=data.groupby('continent').beer_servings.mean()
print(avg_beer)
#每個洲消費葡萄酒(Win) 的最大值、最小值和平均值是多少？
all_state=data.groupby('continent').wine_servings.agg(['max','min','mean'])
print(all_state)


