from importlib.metadata import PackageNotFoundError

import pandas as pd16


from model import *
from visual import Analysis

def main():
    result = Data()
    while True:
        print('\n\n=====================')
        print('1. Show data frame\n'
              '2. Add Smartphone\n'
              '3. Compare\n'
              '4. Delete Smartphone\n'
              '5. Exit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            print('============================')
            Analysis().table()
            print('============================\n\n\n')


        elif choice == 2:
            result.add_smartphone()

        elif choice == 3:
            Analysis().compare()

        elif choice == 4:
            result.delete_data()

        elif choice == 5:
            return

        else:
            raise ValueError



try:
    main()
except ValueError:
    print('Please enter a valid choice')
except IndexError:
    print('Please enter in the range')
except PackageNotFoundError:
    print('Install packages: pandas, matplotlib')
except KeyboardInterrupt:
    print('The program will close')

finally:
    print('The program will close')
