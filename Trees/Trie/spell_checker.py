#### COPIED ###### VERIFIED
from trie import Trie
import time

class SpellChecker:  # Copied
    # chars = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    #    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',  'x', 'y', 'z')
    # Better to define as string and convert to tuple, if needed
    chars = 'abcdefghijklmnopqrstuvwxyz'

    '''
    Creating a trie from dictionary in __init__. Instead of dictionary, we could
    also pass various text files and create a trie out of all the words in the
    texts. With such an approach, we can sort the result with using probability

    import re
    from collections import Counter
    # find all words from text and create a dictionary using 'Counter' which
    # creates dictionary as dict[word] = num_occurance
    def words(text): return re.findall(r'\w+', text.lower())
    WORDS = Counter(words(open('big.txt').read()))

    def P(word, N=sum(WORDS.values())):
        "Probability of `word`."
        return WORDS[word] / N
    '''
    def __init__(self, filename):  # Filename is dictionary
        self.trie = Trie()  # Create a trie of all the words
        with open(filename) as fil:  # Always use 'with' for opening files
            for word in fil:
                word = word.strip().lower()  # strip and convert to lower
                self.trie.insert(word, word)

    # Create a list of words by removing single character at all the position
    @staticmethod
    def get_delete_words(word):
        result = set()  # Use set to avoid duplication
        for i in range(len(word)):
            new_word = word[:i] + word[i + 1:]  # Exclude i'th character
            result.add(new_word)

        return result

    # Create a list of words by replacing a single character.
    @staticmethod
    def get_replace_words(word):
        result = set()
        for i in range(len(word)):
            for j in SpellChecker.chars:  # try replacing with all alphabets
                # word[:len(word)]  will give complete word. But range(len(word)) will
                # give max value of len(word) - 1. So it will exclude the last character
                # as word[: len(word) -1] will exclude last character
                new_word = word[:i] + j + word[i + 1:]
                result.add(new_word)
        return result

    # Add an extra character at all available positions
    @staticmethod
    def get_add_words(word):
        result  = set()
        for i in range(len(word) + 1):  # + 1 is needed to insert as last character
            for j in SpellChecker.chars:
                new_word = word[:i] + j + word[i:]
                result.add(new_word)
        return result

    # interchange two nearby characters and see
    @staticmethod
    def get_transpose_words(word):
        result = set()
        for i in range(len(word) - 1):  # i + 1 should be valid. So use len - 1
            # exchange ith and (i+1)th character
            new_word = word[:i] + word [i + 1] + word[i] + word [i + 2:]
            result.add(new_word)
        return result

    # Generate all the words by having single edit using 4 methods
    def generate_suggestions_edit1(self, word):
        return set.union(self.get_delete_words(word),
                         self.get_replace_words(word),
                         self.get_add_words(word),
                         self.get_transpose_words(word))

    def spell_check(self, word):
        word = word.lower()

        # If the word already exists, there is no need to edit
        if self.trie.find_word(word):
            return word

        # Generate all words by doing only a single character edit
        ret1 = self.generate_suggestions_edit1(word)

        result = []
        for w in ret1:
            if self.trie.find_word(w):
                result.append(w)

        if len(result):
            return result

        '''
        Using union like below is very slow. Use generator and add method
        # edit2 = set()  # Need temporary set as we cannot modify the same ret1 in the below loop
        # for i in ret1:
        #      edit2 = edit2.union(self.generate_suggestions_edit1(i))  # union is Non modifying

        # ret1 = ret1.union(edit2)
        '''

        '''
        edit2 = (e2 for e1 in ret1 for e2 in self.generate_suggestions_edit1(e1))
        print(edit2, ret1)
        for w in edit2:
            ret1.add(w)

        RuntimeError: Set changed size during iteration
        Error because in the for loop, ret1 is modified. The Generator(edit2) will be generating the
        values only in the for loop, using the same ret1
        '''

        # Go for two character edit by going through all words created with single edits
        '''
        Create generator using for loops
        for e1 in ret1.copy():
            for e2 in fn():
                use e2
        '''
        ret2 = set()
        for w in (e2 for e1 in ret1 for e2 in \
                  self.generate_suggestions_edit1(e1)):
            ret2.add(w) # using ret2 to avoid ret1 modification issue

        for w in ret2:
            if self.trie.find_word(w):
                result.append(w)

        return set(result)

if __name__ == '__main__':
    s = SpellChecker('wordlist.txt')

    time1 = time.time()
    print(s.spell_check('diffarance'))
    print(time.time() - time1)