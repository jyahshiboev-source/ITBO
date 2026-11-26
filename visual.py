import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model import *
import random

class Analysis:
    __df = Data().get_df()
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
            self.__bar_chart(self.__df['Name'], self.__df['Points'], 'Name', 'Points')
            print('\n\n\n')
        elif ask == '2':
            self.__bar_chart(self.__df['Processor'], self.__df['Points'], 'Name', 'Points')

    def __bar_chart(self, x, y, lx, ly):
        colors = [(random.random(), random.random(), random.random()) for _ in range(len(x))]

        plt.bar(x, y, color=colors)
        plt.xlabel(lx)
        plt.ylabel(ly)
        plt.show()

    def __bar_charth(self, x, y, lx, ly):
        colors = [(random.random(), random.random(), random.random()) for _ in range(len(x))]

        plt.barh(x, y, color=colors)
        plt.xlabel(lx)
        plt.ylabel(ly)
        plt.show()
