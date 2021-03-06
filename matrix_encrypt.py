"""
Problem Statement

An English text needs to be encrypted using the following encryption scheme. 
First, the spaces are removed from the text. Let L be the length of this text. 
Then, characters are written into a grid, whose rows and columns have the following constraints:

floor(sqrt(L))<=rows<=column=ceil(sqrt(L))
For example, the sentence if man was meant to stay on the ground god would have given us roots after removing spaces is 54 characters long, so it is written in the form of a grid with 7 rows and 8 columns.

ifmanwas  
meanttos          
tayonthe  
groundgo  
dwouldha  
vegivenu  
sroots
Ensure that rows×columns>=L
If multiple grids satisfy the above conditions, choose the one with the minimum area, i.e. rows×columns.
The encoded message is obtained by displaying the characters in a column, inserting a space, and then displaying the next column and inserting a space, and so on. For example, the encoded message for the above rectangle is:

imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import ceil, floor, sqrt

def build_matrix(row,col,string):
    ret = []
    start_row = 0
    value = ''
    for letter in string:
        value = value + letter
        if len(value) >= col:
            ret.append(value)
            value = ''
    if value:
        ret.append(value)
    return ret


def encrypt(input):
    input = input.replace(' ','')
    len_input = len(input)
    sr = sqrt(len_input)
    num_col = int(ceil(sr))
    num_row = int(ceil(float(len_input)/num_col))
    matrix = build_matrix(num_row, num_col, input)

    new_matrix = [''] * num_col
    for i,row in enumerate(matrix):
        for j,letter in enumerate(row):
            new_matrix[j] = new_matrix[j] + letter
    
    return ' '.join(new_matrix)

print encrypt(raw_input())
