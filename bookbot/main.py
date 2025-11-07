"""""
Returns the book as a string in terminal
"""""

import sys
from stats import get_num_words
from stats import create_dictionary
from stats import sort_dictionary

def get_book_text(filepath):
    """ Grab file text as a string """
    with open(filepath) as file:
        string = file.read()
    return string

def print_result(words, dictionary, filepath):
    """ Print the results """
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count -----------")
    print(f"Found {words} total words")
    print("--------- Character Count ---------")
    partition = sort_dictionary(dictionary)
    for letter in partition:
        print(f"{letter["char"]}: {letter["count"]}")
    print("============ END ============")


def main():
    """
    Test system arguments
    Push Frankenstein into get_book_text
    """

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        string = get_book_text(filepath)
        num_words = get_num_words(string)
        dictionary = create_dictionary(string)
        print_result(num_words, dictionary, filepath)

main()
