# Given an input string and a dictionary of words,
# segment the input string into a space-separated
# sequence of dictionary words if possible. For
# example, if the input string is "applepie" and
# dictionary contains a standard set of English words,
# then we would return the string "apple pie" as output.

from collections import deque

import time

def timeit(f):
    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print 'func:%r args:[] took: %2.4f sec' % \
          (f.__name__, te-ts)
        return result

    return timed


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


memoize = {}
def word_separation_dp(word, dictionary):
    if word in dictionary:
        return word
    
    if word in memoize:
        return memoize[word]
    
    for i in range(len(word)):
        prefix = word[0:i]
        suffix = word[i:len(word)]
        
        if prefix in dictionary:
            split_suff = word_separation_dp(suffix, dictionary)
            if split_suff:
                memoize[word] = prefix + ' ' + split_suff
                return prefix + ' ' + split_suff
        
    return None

def word_separation_r(word, dictionary):
    if word in dictionary:
        return word
    
    for i in range(len(word)):
        prefix = word[0:i]
        suffix = word[i:len(word)]
        
        if prefix in dictionary:
            split_suff = word_separation_r(suffix, dictionary)
            if split_suff:
                return prefix + ' ' + split_suff
        
    return None



# Testing

timed_word_sep_dp = timeit(word_separation_dp)
print timed_word_sep_dp('i', ['i', 'like'])
print timed_word_sep_dp('ilike', ['i', 'like', 'apples'])
print timed_word_sep_dp('iloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimals', ['i', 'like', 'love', 'an', 'animal', 'animals'])


timed_word_sep_r = timeit(word_separation_r)
print timed_word_sep_r('iloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimals', ['i', 'like', 'love', 'an', 'animal', 'animals'])
    
    
timed_word_sep = timeit(word_separation)
print timed_word_sep('iloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeloveloveloveanimalsanimalsloveilikeiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimalsiloveanimals', ['i', 'like', 'love', 'an', 'animal', 'animals'])
    
    
# print word_separation('i', ['i', 'like'])
# print word_separation('il', ['i', 'like', 'apples'])
# print word_separation('ilike', ['i', 'like', 'apples'])
# print word_separation('ilikiiiieb', ['i', 'l', 'k', 'e'])
# print word_separation('ilikeapp', ['i', 'like', 'apples'])
# print word_separation('ilikeants', ['i', 'like', 'an', 'ants'])
# print word_separation('iloveanimals', ['i', 'like', 'love', 'an', 'animal', 'animals'])
