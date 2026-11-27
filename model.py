import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=pd.errors.Pandas4Warning)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

class Data:
    __df = pd.read_csv("smartphones.csv", sep=None, engine='python')
    #__df = __df.loc[:, ~__df.columns.str.contains('^Unnamed')]

    def search(self, table, csv, name):
        df = pd.read_csv(str(csv))
        result = df[df[str(table)].str.contains(name, case=False, na=False, regex=False)]
        return result

    def data_integration(self, what, table, csv):

        def table_search(name):
            result = self.search(table, csv, str(name))
            if result.empty:
                print("No cpu found")
                return
            elif len(result) > 1:
                print(result[table].reset_index(drop=True))
                index = str(input(f"Enter name or index of the {what} above: "))
                if index.isdigit() and int(index) <= len(result) and int(index) > -1:
                    print('\n', result.iloc[int(index)][table])

                    if len(result.iloc[int(index)][table]) != None:
                        while True:
                            ask = str(input("\nIs this the processor you choose? (y/n): "))
                            if ask.lower() == 'y':
                                return result.iloc[int(index)]
                            elif ask.lower() == 'n':
                                break
                            else:
                                print("Please enter y or n")
                        return self.data_integration(what, table, csv)
                    else:
                        pass
                elif index.isdigit() and int(index) >= len(result) and int(index) <= -1:
                    print('Index out of range')

                elif index.isdigit() == False:
                    table_search(index)

            elif len(result) == 1:
                print(result[table])
                while True:
                    ask = str(input("Is this the processor you choose? (y/n): "))
                    if ask.lower() == 'y':
                        return result.iloc[0]
                    elif ask.lower() == 'n':
                        pass
                    else:
                        print("Please enter y or n")

        while True:
            name = str(input(f"Enter name of the {what}: "))
            target = table_search(name)
            if target is None:
                pass
            else:
                return target

    def add_smartphone(self):
        print("Enter Details of Smartphone (Specs)")
        name = str(input("Enter Name of the Smartphone: "))
        cpu = self.data_integration('cpu', 'Processor', 'CPU_ranking.csv')
        ram = int(input("Enter RAM of the Smartphone(GB): "))
        storage = int(input("Enter Storage of the Smartphone(GB): "))
        camera = int(input("Enter Camera of the Smartphone(MP): "))
        battery = int(input("Enter Battery of the Smartphone(mAh): "))
        display = self.data_integration('Display', 'Panel type', 'Display_ranking.csv')
        size = float(input("Enter Size of the Smartphone's display(inch): ").strip().replace(',', '.'))
        price = float(input("Enter Price of the Smartphone($): ").strip().replace(',', '.'))
        cpu_points = int(cpu['Rating'])
        display_points = float(display['Points'])

        points = (ram * 2 + cpu_points + storage / 16 +
                  camera / 4 + battery / 100 + display_points +
                  size * 3 - price / 10) / 2

        new_row = {
            "Name": name,
            "Processor": cpu['Processor'],
            "RAM": ram,
            "Storage": storage,
            "Camera": camera,
            "Battery": battery,
            "Display": display['Panel type'],
            "Display_size": size,
            "Price": price,
            "Points": points,
            "Cpu_points": cpu_points,
            "Display_points": display_points
        }

        self.__df.loc[len(self.__df)] = new_row
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
