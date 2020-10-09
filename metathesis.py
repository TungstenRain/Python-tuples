"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 12: Tuples in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
def signature(s):
    """
        Returns the signature of this string.
        Signature is a string that contains all of the letters in order.
        
        s: string
        
        return: string; a string that contains all of the letters in order
    """
    # TODO: rewrite using sorted()
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams(filename):
    """
        Finds all anagrams in a list of words.
    
        filename: string filename of the word list
        
        return: a map from each word to a list of its anagrams.
    """
    # initialize values
    d = {}
    fin = open(filename)

    for line in fin:
        word = line.strip().lower()
        t = signature(word)

        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    
    # close the file
    fin.close()

    return d


def print_anagram_sets(d):
    """
        Prints the anagram sets in d.
        
        d: map from words to list of their anagrams


    """
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)


def print_anagram_sets_in_order(d):
    """
        Prints the anagram sets in d in decreasing order of size.
        
        d: map from words to list of their anagrams
    """
    # make a list of (length, word pairs)
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    # sort in ascending order of length
    t.sort()

    # print the sorted list
    for x in t:
        print(x)


def filter_length(d, n):
    """
        Select only the words in the dictionary that have 'n' number of letters.
        
        d: map from word to list of anagrams
        n: integer, number of letters

        return: dictionary
    """
    res = {}
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res

def metathesis_pairs(d):
    """
        Print all pairs of words that differ by swapping two letters.
        
        d: map from word to list of anagrams
    """
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_distance(word1, word2) == 2:
                    print(word1, word2)


def word_distance(word1, word2):
    """
        Computes the number of differences between two words.
        
        word1: strings
        word2: strings

        returns: integer
    """
    assert len(word1) == len(word2)

    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1

    return count


if __name__ == '__main__':
    sets = all_anagrams('words.txt')
    metathesis_pairs(sets)