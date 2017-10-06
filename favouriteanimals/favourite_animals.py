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
        d = Animal_lister()
        if len(argv) == 1:
            v = View()
            v.print_options()
        else:
            print("\nSorry, you have entered an incorrect command. Try this next time: \"python favourite_animals.py\" :)")

class View:
    def __init__(self):
        self.d = Animal_lister()

    def print_options(self):
        print("\nfav_animals:\n")
        for animal in self.d.animals_list:
            print(animal)


class Animal_lister:
    def __init__(self):
        self.animals_list = self.make_list()

    def make_list(self):
        animals_list = []
        with open("favourites.txt", "r") as animals:
            for animal in animals:
                if animal not in animals_list:
                    animals_list.append(animal)
        return animals_list

run = Controller()