import pandas as pd
tubes=pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/youtube-channels-data-from-socialblade.csv')
#將欄位rank轉為數字型態
tubes['Rank']=tubes['Rank'].str[0:-2].str.replace(',','').astype('int')
#將欄位subscribers轉為數字型態
#直接轉換會出錯 因為有'--'這在欄位中
# tubes['Subscribers'].astype('int')
#找出'--'的資料
tubes[tubes['Subscribers'].str.contains('--')].index
#用drop axis=index為刪除index的資料 inplace=true為直接刪除不保留
tubes.drop(labels=tubes[tubes['Subscribers'].str.contains('--')].index,axis='index',inplace=True)
#再將欄位subscribers轉為數字型態
tubes['Subscribers'].astype('int')
#看grade欄位有幾種等級 
tubes['Grade'].unique()
#轉換數值 map
grade_map={'A++ ':5,'A+ ':4,'A ':3,'A- ':2,'B+ ':1}
tubes['Grade']=tubes['Grade'].map(grade_map)
