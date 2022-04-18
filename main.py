from colorama import init
from colorama import Back
from termcolor import colored
import time
import os


init()


menu_options = {
    1: 'Create database',
    2: 'delete column',
    3: 'Insert to database',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print(Back.BLUE)
        print (key, '--', menu_options[key] )

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print(Back.red + 'Wrong Input. ')
            print(Back.BLACK + '')
        if option == 1:
         os.system('create.py')  
        elif option == 2:
         os.system('drop.py')
        elif option == 3:
         os.system('insert.py')
        elif option == 4:
            print('Goodbye!')
            exit()
        else:
            print(Back.RED + 'ERROR 404 NOT FOUND')
            print(Back.BLACK + '')