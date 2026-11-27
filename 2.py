import pandas as pd
from matplotlib import pyplot as plt
from pandas import read_csv
from model import *
from pandas.plotting import table

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

dfs = read_csv("smartphones.csv")
#dfs = dfs.loc[:, ~dfs.columns.str.contains('^Unnamed')]

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
#s = dfs.iloc['Name']
#print(s)

#cpu = Data().data_integration('Display', 'Panel type', 'Display_ranking.csv')
#print(float(cpu['Points']) + float(cpu['Points'] ))

#print("Enter Details of Smartphone (Specs)")
#name = str(input("Enter Name of the Smartphone: "))
#print(type(name))
#cpu = Data().data_integration('cpu', 'Processor', 'CPU_ranking.csv')
#print(type(cpu))
#ram = int(input("Enter RAM of the Smartphone(GB): "))
#print(type(ram))
#storage = int(input("Enter Storage of the Smartphone(GB): "))
#print(type(storage))
#camera = int(input("Enter Camera of the Smartphone(MP): "))
#print(type(camera))
#battery = int(input("Enter Battery of the Smartphone(mAh): "))
#print(type(battery))
#display = Data().data_integration('Display', 'Panel type', 'Display_ranking.csv')
#print(type(display))
#size = float(input("Enter Size of the Smartphone's display(inch): ").strip().replace(',', '.'))
#print(type(size))
#price = float(input("Enter Price of the Smartphone($): ").strip().replace(',', '.'))
#print(type(price))
#cpu_points = int(cpu['Rating'])
#print(cpu_points)
#print(type(cpu_points))
#display_points = float(display['Points'])
#print(display_points)
#print(type(display_points))

#print(dfs['CPU_points'])
#print(type(dfs['CPU_points']))

fig, ax = plt.subplots(figsize=(12,4))
ax.axis('off')
tbl = table(ax, dfs, loc='center', cellLoc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(9)
tbl.scale(1, 1.6)
tbl.auto_set_column_width(col=list(range(len(dfs.columns))))
plt.tight_layout()
plt.show()