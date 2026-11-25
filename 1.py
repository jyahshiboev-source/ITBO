import pandas as pd
import warnings
from pandas import DataFrame

warnings.simplefilter(action='ignore', category=pd.errors.Pandas4Warning)

class Smartphone:
    __df = DataFrame({'Name' : [],
                      'Processor' : [],
                      'RAM' : [],
                      'Storage' : [],
                      'Camera' : [],
                      'Battery' : [],
                      'Display' : [],
                      'Price' : [] ,
                      'Points' : []})

    def processor_search(self):
        df = pd.read_csv('CPU_ranking.csv')

    def add_smartphone(self):
        print("Enter Details of Smartphone (Specs)")
        name = str(input("Enter Name of the Smartphone: "))
        ram = int(input("Enter RAM of the Smartphone(GB): "))
        storage = int(input("Enter Storage of the Smartphone(GB): "))
        camera = int(input("Enter Camera of the Smartphone(MP): "))
        battery = int(input("Enter Battery of the Smartphone(mAh): "))
        display = float(input("Enter Display of the Smartphone: "))
        price = float(input("Enter Price of the Smartphone($): "))

        points = (ram * 2 + storage / 16 +
                  camera / 4 + battery / 200 +
                  display * 3 - price / 10) / 2

        self.__df.loc[len(self.__df)] = [name, ram, storage, camera, battery, display, price, points]

    def get_df(self):
        return self.__df

    def get_points(self):
        return self.__df.groupby('Name', as_index=False)['Points'].sum()
class Analyzer(Smartphone):
    def points(self):
        pass


def main():
    result = Analyzer()
    while True:
        print('1. Show data frame\n'
              '2. Add Smartphone\n'
              '3. value score\n'
              '4. Exit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            print('============================')
            print(result.get_df().head())
            print('============================\n\n\n')


        elif choice == 2:
            result.add_smartphone()

        elif choice == 3:
            print(result.get_points())

        elif choice == 4:
            return

        else:
            raise ValueError
try:
    main()
except ValueError:
    print('Please enter a valid choice')
