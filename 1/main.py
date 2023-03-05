import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("australian.txt", sep=" ", header=None)
print(df)
df.columns = [
    "a1 s",
    "a2 n",
    "a3 n",
    "a4 s",
    "a5 s",
    "a6 s",
    "a7 n",
    "a8 s",
    "a9 s",
    "a10 n",
    "a11 s",
    "a12 s",
    "a13 n",
    "a14 n",
    "y n"
]
print(df)
print(df.describe())
for column in df.columns:
    print(column, pd.unique(df[column]))

df2 = df.loc[:, df.columns != "y n"]
for column in df.columns[:-1]:
    random_rows = df2.sample(frac=0.1).index
    df2.loc[random_rows, column] = '?'

print(df2)

for column in df.columns[:-1]:
    count = len(df2[df2[column] == "?"])
    print(f'{column}: {count}')

df2.replace(to_replace='?', value=np.nan, inplace=True)
df2.apply(lambda x: x.fillna(x.mean()),axis=0)

scaler = MinMaxScaler(feature_range=(-1, 1))
df_norm = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print(df_norm)

scaler = MinMaxScaler(feature_range=(0, 1))
df_norm = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print(df_norm)

ndf=(df-df.min())/(df.max()-df.min()) * 10
print(ndf)

new_df = pd.read_csv("Churn_Modelling.csv")
new_df.head()

ddf = pd.get_dummies(new_df['Geography'])
print(ddf)
ndf = pd.concat([new_df, ddf], axis=1)
print(ndf)