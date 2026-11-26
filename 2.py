import pandas as pd
from pandas import read_csv

df = read_csv("CPU_ranking.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#name = str(input("Enter name of the cpu: "))
#result = df[df['Processor'].str.contains(name, case=False, na=False)]
#if result.empty:
#    print("No cpu found")
#elif len(result) > 1:
#    print("Choose one of these processors:")
#    print(result['Processor'])
#elif len(result) == 1:
#    print(result['Processor'])
#    group = result.groupby(['Processor'])['Rating'].sum()
#    print(group)

#print(df)
#result = df.groupby(['Processor'])['Rating'].sum()
#dff = df.loc[0]
#print(df.loc[0])

dfs = read_csv("smartphones.csv", sep=None, engine='python')
dfs = dfs.loc[:, ~dfs.columns.str.contains('^Unnamed')]

#print("Enter Details of Smartphone (Specs)")
#name = str(input("Enter Name of the Smartphone: "))
#cpu = 'Snap'
#ram = int(input("Enter RAM of the Smartphone(GB): "))
#storage = int(input("Enter Storage of the Smartphone(GB): "))
#camera = int(input("Enter Camera of the Smartphone(MP): "))
#battery = int(input("Enter Battery of the Smartphone(mAh): "))
#display = float(input("Enter Display of the Smartphone: "))
#price = float(input("Enter Price of the Smartphone($): "))
#points = (ram * 2 + storage / 16 + camera / 4 + battery / 200 + display * 3 - price / 10)
#
#
#dfs.loc[len(dfs)] = [name, cpu, ram, storage, camera, battery, display, price, points]
##dfs = dfs.drop(index=0)
#dfs.to_csv("Smartphones.csv", index=False)
#
##print(dfs)
s = dfs.iloc['Name']
print(s)


