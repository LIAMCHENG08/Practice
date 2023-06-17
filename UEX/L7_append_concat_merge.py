#append
import pandas as pd

df1 = pd.DataFrame({'A':['A0', 'A1', 'A2', 'A3'],
                       'B':['B0', 'B1', 'B2', 'B3'],
                       'C':['C0', 'C1', 'C2', 'C3'],
                       'D':['D0', 'D1', 'D2', 'D3']},
                      index = [0, 1, 2, 3])

df2 = pd.DataFrame({'A':['A4', 'A5', 'A6', 'A7'],
                       'B':['B4', 'B5', 'B6', 'B7'],
                       'C':['C4', 'C5', 'C6', 'C7'],
                       'D':['D4', 'D5', 'D6', 'D7']},
                      index = [4, 5, 6, 7])

df1.append(df2)

df3 = pd.DataFrame({'A':['A8', 'A9', 'A10', 'A11'],
                     'B':['B8', 'B9', 'B10', 'B11'],
                     'C':['C8', 'C9', 'C10', 'C11'],
                     'D':['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])

df1.append([df2, df3])

df4 = pd.DataFrame({'B':['B2', 'B3', 'B6', 'B7'],
                   'D':['D2', 'D3', 'D6', 'D7'],
                   'F':['F2', 'F3', 'F6', 'F7']},
                  index = [2, 3, 6, 7])
#索引值有誤
df1.append(df4)
#把索引值變成正常排序
df1.append(df4,ignore_index=True)

#loc 新增資料
df1.loc[4]=['A4','B4','C4','D4']

df1=df1.append({'A':'A5','B':'B5','C':'C5','D':'D5'},ignore_index=True)

#%%
#concat
import pandas as pd

# 將df1, df2, df3 在index軸的方向上做聯集
df1 = pd.DataFrame({'A':['A0', 'A1', 'A2', 'A3'],
                   'B':['B0', 'B1', 'B2', 'B3'],
                   'C':['C0', 'C1', 'C2', 'C3'],
                   'D':['D0', 'D1', 'D2', 'D3']},
                  index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A':['A4', 'A5', 'A6', 'A7'],
                   'B':['B4', 'B5', 'B6', 'B7'],
                   'C':['C4', 'C5', 'C6', 'C7'],
                   'D':['D4', 'D5', 'D6', 'D7']},
                  index=[4, 5, 6, 7])
df3 = pd.DataFrame({'A':['A8', 'A9', 'A10', 'A11'],
                   'B':['B8', 'B9', 'B10', 'B11'],
                   'C':['C8', 'C9', 'C10', 'C11'],
                   'D':['D8', 'D9', 'D10', 'D11']},
                  index=[8, 9, 10, 11])
pd.concat([df1, df2, df3])

# 將df1, df4 在column軸的方向上做聯集
df4 = pd.DataFrame({'B':['B2', 'B3', 'B6', 'B7'],
                   'D':['D2', 'D3', 'D6', 'D7'],
                   'F':['F2', 'F3', 'F6', 'F7']},
                  index=[2, 3, 6, 7])

pd.concat([df1, df4], axis=1, join='outer', sort=False )
# 將df1, df4 在column軸的方向上做交集
pd.concat([df1,df4],axis=1,join='inner',sort=False)
# 將df1, df4 在index軸的方向上做交集
pd.concat([df1,df4],axis=0,join='inner',sort=False)
# 群組化索引值
# keys=['次索引值1', '次索引值2', ...]
result=pd.concat([df1,df2,df3],keys=['x','y','z'])
print(result)

result.loc['y']
#%%
#merge
import pandas as pd

# 基於特定欄位合併資料merge
# 左邊DataFrame.merge(右邊DataFrame, on='key欄位')
# 如果沒有指定key欄位，兩個dataframe重複的欄位將會被指定為key欄位
left = pd.DataFrame({'key':['K0', 'K1', 'K2', 'K3'],
                    'A':['A0', 'A1', 'A2', 'A3'],
                    'B':['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key':['K0', 'K1', 'K2', 'K3'],
                     'C':['C0', 'C1', 'C2', 'C3'],
                     'D':['D0', 'D1', 'D2', 'D3']})
left.merge(right, on='key')
# 兩個key欄位
left = pd.DataFrame({'key1':['K0', 'K0', 'K1', 'K2'],
                    'key2':['K0', 'K1', 'K0', 'K1'],
                    'A':['A0', 'A1', 'A2', 'A3'],
                    'B':['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1':['K0', 'K1', 'K1', 'K2'],
                     'key2':['K0', 'K0', 'K0', 'K0'],
                     'C':['C0', 'C1', 'C2', 'C3'],
                     'D':['D0', 'D1', 'D2', 'D3']})
left.merge(right, on=['key1', 'key2'])
# 參數how有四種設定值
left.merge(right,how='left',on=['key1','key2'])
left.merge(right,how='right',on=['key1','key2'])
left.merge(right,how='inner',on=['key1','key2'])
left.merge(right,how='outer',on=['key1','key2'])
# 參數indicator設定為True，新增分類類型欄位
#可以知道左邊有 還是交集 還是右邊有
left.merge(right,how='outer',on=['key1','key2'],indicator=True)

# 欄位相同，但並未被指定為key
# 系統會自動產生_x, _y 的後綴詞
left.merge(right,on='key1')
# 自己定義後綴詞的名稱
# 使用參數suffixes定義後綴詞的名稱
left.merge(right,on='key1',suffixes=('_left','_right'))





