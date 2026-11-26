import pandas as pd
import warnings
from pandas import DataFrame

warnings.simplefilter(action='ignore', category=pd.errors.Pandas4Warning)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

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

    def search(self, table, csv, name):
        df = pd.read_csv(str(csv))
        result = df[df[str(table)].str.contains(name, case=False, na=False, regex=False)]
        return result

    def processor_integration(self):
        while True:
            name = str(input("Enter name of the cpu: "))
            cpu = self.processor_search(name)
            if cpu is None:
                pass
            else:
                return cpu

    def processor_search(self, name):
        result = self.search('Processor', 'CPU_ranking.csv', str(name))
        if result.empty:
            print("No cpu found")
            return
        elif len(result) > 1:
            print(result['Processor'].reset_index(drop=True))
            print("========================\n"
                  "Choose one of these processors:")
            index = str(input("Enter name or index of the cpu above: "))
            if index.isdigit():
                print(result.iloc[int(index)]['Processor'])
                if len(result.iloc[int(index)]['Processor']) != None:
                    while True:
                        ask = str(input("Is this the processor you choose? (y/n): "))
                        if ask.lower() == 'y':
                            return result.loc[int(index)]
                        elif ask.lower() == 'n':
                            break
                        else:
                            print("Please enter y or n")

                else:
                    pass
            elif index.isdigit() == False:
                self.processor_search(index)

        elif len(result) == 1:
            print(result['Processor'])
            while True:
                ask = str(input("Is this the processor you choose? (y/n): "))
                if ask.lower() == 'y':
                    return result.loc[0]
                elif ask.lower() == 'n':
                    pass
                else:
                    print("Please enter y or n")

    def add_smartphone(self):
        print("Enter Details of Smartphone (Specs)")
        name = str(input("Enter Name of the Smartphone: "))
        cpu = self.processor_integration()
        ram = int(input("Enter RAM of the Smartphone(GB): "))
        storage = int(input("Enter Storage of the Smartphone(GB): "))
        camera = int(input("Enter Camera of the Smartphone(MP): "))
        battery = int(input("Enter Battery of the Smartphone(mAh): "))
        display = float(input("Enter Display of the Smartphone: "))
        price = float(input("Enter Price of the Smartphone($): "))

        points = (ram * 2 + int(cpu['Rating']) + storage / 16 +
                  camera / 4 + battery / 200 +
                  display * 3 - price / 10) / 2

        self.__df.loc[len(self.__df)] = [name, cpu['Processor'], ram, storage, camera, battery, display, price, points]

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
            print(result.get_df().loc[result.get_df()["Name"] != None, ['Name','Processor', 'RAM', 'Storage', 'Camera', 'Battery', 'Display', 'Price']])
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
