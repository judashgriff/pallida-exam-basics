# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases
# print(unique_characters("anagram"))
# Should print out:
# ["n", "g", "r", "m"]

def unique_characters(string):
    unique_chars_list = []
    for letter in string.replace(" ", ""):
        if letter not in unique_chars_list:
            unique_chars_list.append(letter)
    return unique_chars_list

print(unique_characters("anagram"))