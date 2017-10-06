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
        d = Dictionary()
        animals_list = d.make_dictionary()
            if len(argv) == 1:
                v = View()
                v.print_options()
            else:
                self.select_operation(animals_list)

class View:
    def __init__(self):
        d = Dictionary()

    def print_options(self):
        print("fav_animals")
        for animal in d.animals_list:
            print(animal)


class Dictionary:
    def __init__(self):
        self.animals_list = []

    def make_dictionary(self):
        with open("favourites.txt", "r") as animals:
            for line in animals:
                if line not in self.animals_list:
                    self.animals_list.append(line)
