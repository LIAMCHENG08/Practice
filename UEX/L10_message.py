import pandas as pd

data=pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/msg.txt',
                 sep='\t',
                 names=['status','msg'])

data['status'].str.upper()
data['msg'][0].upper()

data['msg'].str.title()

data['msg'].str.len()

data['status'].str.replace('ham','not spam')

data['msg'].str.split(',')[0]

data['msg'].str.startswith('a')

data.loc[data.msg.str.startswith('a')]

data[data['msg'].str.startswith('a')]

ham=data[data['status']=='ham']

mask=ham['msg'].str.contains('OK')

ham[mask]

data.columns.str.upper()

data.columns=data.columns.str.upper()
