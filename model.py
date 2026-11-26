import pandas as pd
import warnings
from pandas import DataFrame

warnings.simplefilter(action='ignore', category=pd.errors.Pandas4Warning)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

class Data:
    __df = pd.read_csv("smartphones.csv", sep=None, engine='python')
    __df = __df.loc[:, ~__df.columns.str.contains('^Unnamed')]

    def search(self, table, csv, name):
        df = pd.read_csv(str(csv))
        result = df[df[str(table)].str.contains(name, case=False, na=False, regex=False)]
        return result

    def processor_integration(self):

        def processor_search(name):
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
                    if int(index) <= len(result) and int(index) > -1:
                        print(result.iloc[int(index)]['Processor'])
                        if len(result.iloc[int(index)]['Processor']) != None:
                            while True:
                                ask = str(input("Is this the processor you choose? (y/n): "))
                                if ask.lower() == 'y':
                                    return result.iloc[int(index)]
                                elif ask.lower() == 'n':
                                    break
                                else:
                                    print("Please enter y or n")
                        else:
                            pass
                    else:
                        print('Index out of range')

                elif index.isdigit() == False:
                    processor_search(index)

            elif len(result) == 1:
                print(result['Processor'])
                while True:
                    ask = str(input("Is this the processor you choose? (y/n): "))
                    if ask.lower() == 'y':
                        return result.iloc[0]
                    elif ask.lower() == 'n':
                        pass
                    else:
                        print("Please enter y or n")

        while True:
            name = str(input("Enter name of the cpu: "))
            cpu = processor_search(name)
            if cpu is None:
                pass
            else:
                return cpu

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
        self.__df.to_csv("Smartphones.csv", index=False)

    def get_df(self):
        return self.__df

    def get_points(self):
        return self.__df.groupby('Name', as_index=False)['Points'].sum()

    def delete_data(self):
        print(self.__df.loc[
                  self.__df["Name"] != None, ['Name', 'Processor', 'RAM', 'Storage', 'Camera', 'Battery',
                                                    'Display', 'Price']])
        print('=====================================================')
        print('=====================================================')
        print('=====================================================')
        index = int(input('\n Choose the index of the Smartphone you want to delete from above: '))
        self.__df = self.__df.drop(index=index)
        self.__df.to_csv("Smartphones.csv", index=False)
