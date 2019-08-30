import pandas as pd

df1['i'] = list(range(0,len(df1.index)*2,2)) # 偶数
df2['i'] = list(range(1,len(df2.index)*2,2)) # 奇数

df = pd.concat([df1, df2])

df = df.sort_values('i').reset_index(drop=True).drop('i',axis=1)