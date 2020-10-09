"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 12: Tuples in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
# Globals
"""
    The variable memo is a dictionary that maps from each word that is known to be reducible to a list of its reducible children.  It starts with the empty string.
"""
memo = {}
memo[''] = ['']


def make_word_dict():
    """
        Reads a word list and returns a dictionary.

        return: dictionary
    """
    # initialize variables
    a_dictionary = dict()

    # open the file
    fin = open('words.txt')

    for line in fin:
        word = line.strip().lower()
        a_dictionary[word] = None

    for letter in ['a', 'i', '']:
        a_dictionary[letter] = letter

    # close the file
    fin.close()

    return a_dictionary



def is_reducible(word, word_dict):
    """
        If word is reducible, returns a list of its reducible children.
        Also adds an entry to the memo dictionary.
        Definition: A string is reducible if it has at least one child that is reducible.  The empty string is also reducible.
    
        word: string
        word_dict: dictionary with words as keys

        return: list; reducible children from a word
    """
    # Determine if word has been checked, if it has don't continue
    if word in memo:
        return memo[word]

    # check each of the children and make a list of the reducible ones
    result = []
    for child in children(word, word_dict):
        if is_reducible(child, word_dict):
            result.append(child)

    # memoize and return the result
    memo[word] = result
    return result


def children(word, word_dict):
    """
        Returns a list of all words that can be formed by removing one letter.

        word: string
        
        return: list of strings
    """
    result = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in word_dict:
            result.append(child)
    return result


def all_reducible(word_dict):
    """
        Checks all words in the word_dict; returns a list reducible ones.
        word_dict: dictionary with words as keys
    """
    result = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []:
            result.append(word)
    return result


def print_trail(word):
    """
        Prints the sequence of words that reduces this word to the empty string.
        If there is more than one choice, it chooses the first.
        
        word: string
    """
    if len(word) == 0:
        return
    print(word, end=' ')
    t = is_reducible(word, word_dict)
    print_trail(t[0])


def print_longest_words(word_dict):
    """
        Finds the longest reducible words and prints them.
        
        word_dict: dictionary of valid words
    """
    words = all_reducible(word_dict)

    # use DSU to sort by word length
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)

    # print the longest 5 words
    for _, word in t[0:5]:
        print_trail(word)
        print('\n')


if __name__ == '__main__':
    word_dict = make_word_dict()
    print_longest_words(word_dict)