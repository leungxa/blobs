# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

#     Only one letter can be changed at a time
#     Each intermediate word must exist in the word list

# For example,

# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5. 

from collections import deque

def one_letter_diff(word1, word2):
    count = 0
    if len(word1) != len(word2):
        return False
    for i in range(len(word1)):
        if count == 2:
            return False
        if word1[i] != word2[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False

class Node():
    def __init__(self, value, word_list):
        self.value = value
        self.word_list = word_list
    
def word_ladder(begin_word, end_word, word_list):
    if begin_word == end_word:
        return 1
    begin_node = Node(begin_word, word_list)
    word_q = deque([begin_node])
    level = 1
    nodes_on_level = 1
    while len(word_q):
        if nodes_on_level == 0:
            nodes_on_level = len(word_q)
            level += 1
        curr_node = word_q.popleft()
        new_begin = curr_node.value
        nodes_on_level -= 1
        if one_letter_diff(new_begin, end_word):
            return level + 1
        for list_word in word_list:
            if one_letter_diff(new_begin, list_word):
                new_node = Node(list_word, [x for x in word_list if x != list_word])
                word_q.append(new_node)

# test
# print one_letter_diff("hot", "hit")
# print one_letter_diff("hoot", "hit")
# print one_letter_diff("dot", "hit")

begin_word = "hit"
end_word = "cog"
word_list = ["hot","dot","lot", "lit", "lim", "kim", "dog", "kog", "log", "a", "b", "c"]
print word_ladder(begin_word, end_word, word_list)
print word_ladder("dot", end_word, word_list)
print word_ladder("don", "hog", word_list)
print word_ladder("d", "g", word_list)
print word_ladder("d", "d", word_list)
