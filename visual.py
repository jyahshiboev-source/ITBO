import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import table
from model import *
import random

class Analysis:
    __df = Data().get_df()
    __dfs = __df.loc[__df["Name"] != None, ['Name', 'Processor', 'RAM', 'Storage', 'Camera', 'Battery',
                                                        'Display', 'Display_size', 'Price']]
    def compare(self):
        print('1. Comparing Smartphones by points\n'
              '2. Compare Processors\n'
              '3. Compare RAM\n'
              '4. Compare Storage\n'
              '5. Compare Camera\n'
              '6. Compare Battery\n'
              '7. Compare Display\n'
              '8. Compare Price\n'
              '9. Exit')
        ask = str(input('Enter your choice: '))
        if ask == '1':
            self.__bar_chart(self.__df['Name'], self.__df['Points'], 'Name', 'Points', 'Comparison of smartphones by points')
            print('\n\n\n')

        elif ask == '2':
            self.__bar_charth(self.__df['Name'], self.__df['Cpu_points'].astype(float), 'Points', 'Name', 'Comparison of smartphones by cpu points')
            print('\n\n\n')

        elif ask == '3':
            self.__bar_chart(self.__df['Name'], self.__df['RAM'], 'Name', 'GB', 'Comparison of smartphones by RAM')
            print('\n\n\n')

        elif ask == '4':
            self.__bar_chart(self.__df['Name'], self.__df['Storage'], 'Name', 'GB', 'Comparison of smartphones by Storage')
            print('\n\n\n')

        elif ask == '5':
            self.__bar_chart(self.__df['Name'], self.__df['Camera'], 'Name', 'MP', 'Comparison of smartphones by Camera')
            print('\n\n\n')

        elif ask == '6':
            self.__bar_chart(self.__df['Name'], self.__df['Battery'], 'Name', 'mAh', 'Comparison of smartphones by Battery3')
            print('\n\n\n')

        elif ask == '7':
            self.__bar_charth(self.__df['Name'], self.__df['Display_points'], 'Name', 'Points', 'Comparison of smartphones by Display')
            print('\n\n\n')

        elif ask == '8':
            self.__bar_charth(self.__df['Name'], self.__df['Price'], 'Name', 'Points', 'Comparison of smartphones by Price')
            print('\n\n\n')

        elif ask == '9':
            pass
    def __bar_chart(self, x, y, lx, ly, title):
        colors = [(random.random(), random.random(), random.random()) for _ in range(len(x))]

        plt.bar(x, y, color=colors, label=y)
        plt.title(title)
        plt.xlabel(lx)
        plt.ylabel(ly)
        plt.show()

    def __bar_charth(self, x, y, lx, ly, title):
        colors = [(random.random(), random.random(), random.random()) for _ in range(len(x))]

        plt.barh(x, y, color=colors)
        plt.title(title)
        plt.xlabel(lx)
        plt.ylabel(ly)
        plt.show()

    def table(self):
        fig, ax = plt.subplots(figsize=(12, 4))
        ax.axis('off')
        tbl = table(ax, self.__dfs, loc='center', cellLoc='center')
        tbl.auto_set_font_size(False)
        tbl.set_fontsize(9)
        tbl.scale(1, 1.6)
        tbl.auto_set_column_width(col=list(range(len(self.__dfs.columns))))
        plt.tight_layout()
        plt.show()
