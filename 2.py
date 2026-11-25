import pandas as pd
from pandas import read_csv

df = read_csv("CPU_ranking.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

name = str(input("Enter name of the cpu: "))
result = df[df['Processor'].str.contains(name, case=False, na=False)]
if result.empty:
    print("No cpu found")
elif len(result) > 1:
    print("Choose one of these processors:")
    print(result['Processor'])
elif len(result) == 1:
    print(result['Processor'])