"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 12: Tuples in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
def make_histogram(s):
    """
        Make a map from letters to numbers of times they appear (histogram)

        s: string

        return: map of letter to frequency
    """
    # initialize a dictionary
    histogram = {}

    for x in s:
        histogram[x] = histogram.get(x, 0) + 1
    return histogram


def most_frequent(s):
    """
        Sort letters in order of reverse frequency

        s: string

        return: list of letters
    """
    # initialize variables
    histogram = make_histogram(s)
    t = []
    result = []

    for x, freq in histogram.items():
        t.append((freq, x))

    t.sort(reverse=True)

    for freq, x in t:
        result.append(x)
    
    return result


def read_file(filename):
    """
        Opens a file, reads it, and returns the contents of a file as a string

        filename: filename

        return: string
    """
    return open(filename).read()


if __name__ == "__main__":
    # initialize variables
    english = read_file("random_english.txt")
    finnish = read_file("random_finnish.txt")
    french = read_file("random_french.txt")
    portuguese = read_file("random_portuguese.txt")
    
    letter_seq_english = most_frequent(english)
    letter_seq_finnish = most_frequent(finnish)
    letter_seq_french = most_frequent(french)
    letter_seq_portuguese = most_frequent(portuguese)

    print("The most common letters from random_english.txt are:")
    for x in letter_seq_english:
        print(x)
    
    print("The most common letters from random_finnish.txt are:")
    for x in letter_seq_finnish:
        print(x)

    print("The most common letters from random_french.txt are:")
    for x in letter_seq_french:
        print(x)

    print("The most common letters from random_portuguese.txt are:")
    for x in letter_seq_portuguese:
        print(x)