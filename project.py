import pandas as pd

df=pd.read_csv('total_stars.csv')

print(df)
print(df.columns)

df = df.dropna()
print(df)

df.reset_index(drop=True,inplace=True)
print(df)
df.describe()

df.info()
df.head(5)
df.dtypes

df.to_csv('stars.csv')