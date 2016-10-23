# Given an input string and a dictionary of words,
# segment the input string into a space-separated
# sequence of dictionary words if possible. For
# example, if the input string is "applepie" and
# dictionary contains a standard set of English words,
# then we would return the string "apple pie" as output.

from collections import deque

class Phrase:
    def __init__(self, words, rest):
        self.words = words
        self.rest = rest

def is_valid_phrase(words, dictionary):
    for word in words:
        if word not in dictionary:
            return False
    return True

def word_separation(word, dictionary):
    if word in dictionary:
        return word
    root = Phrase([word[0]], word[1:])
    queue = deque([root])

    while len(queue):
        phrase = queue.pop()
        valid = is_valid_phrase(phrase.words, dictionary)
        if phrase.rest:
            next_letter = phrase.rest[0]
            new_words = []
            if valid:
                new_words.append(phrase.words + [next_letter])
            new_words.append(phrase.words[:-1] + [phrase.words[-1] + next_letter])
            for new_word in new_words:
                new_phrase = Phrase(new_word, phrase.rest[1:])
                queue.append(new_phrase)
        elif not phrase.rest and valid:
            return ' '.join(phrase.words)
    return None
        
print word_separation('i', ['i', 'like'])
print word_separation('il', ['i', 'like', 'apples'])
print word_separation('ilike', ['i', 'like', 'apples'])
print word_separation('ilikeapp', ['i', 'like', 'apples'])
print word_separation('ilikeants', ['i', 'like', 'an', 'ants'])
print word_separation('iloveanimals', ['i', 'like', 'love', 'an', 'animal', 'animals'])
