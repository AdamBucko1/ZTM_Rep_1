# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from cat_main import *
from pets_main import *
def main():
    CatMain()
    cats=my_cats
    instanceOfPets=Pets([cats])
    for Cat in instanceOfPets:
        instanceOfPets.walk()

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
