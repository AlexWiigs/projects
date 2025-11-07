"""
Stats file for bookbot
"""

def get_num_words(string):
    """ Get the number of words in a string """
    words = len(string.split())
    return words

def sort_on(items):
    """ Specify values to sort by """
    return items["count"]

def create_dictionary(string):
    """ Take string and return the number of times each character appears """
    string_lower = string.lower() # lowercase the letters
    dictionary = {}
    words = string_lower.split()  # split string into a list of words
    for word in words:
        for letter in word:
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
    return dictionary

def sort_dictionary(dictionary):
    """ Input a dictionary and returns it as a string of sorted dictionaries"""
    partition = []
    for key in dictionary:
        partition.append({"char": key, "count": dictionary[key]})
    partition.sort(reverse=True, key=sort_on)
    return partition
