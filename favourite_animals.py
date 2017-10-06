# The program's aim is to collect your favourite animals and store them in a text file.
# There is a given text file called '''favourites.txt''', it will contain the animals
# If ran from the command line without arguments
# It should print out the usage:
# ```fav_animals [animal] [animal]```
# You can add as many command line arguments as many favourite you have.
# One animal should be stored only at once
# Each animal should be written in separate lines
# The program should only save animals, no need to print them

from sys import argv

class Controller:
    def __init__(self):
        if len(argv) == 1:
            v = View()
            v.print_options()
        else:
            d = Dictionary()
            animals_list = d.make_dictionary()
            self.select_operation(animals_list)

class View:
    
    def print_options(self):
        


class Dictionary:

    def make_dictionary(self):
        pass