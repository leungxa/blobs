# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

# For example,

# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].


def repeated_substrings(s):
    once = set([])
    answers = set()
    
    for i in range(len(s)-9):
        new_word = s[i:i+10]
        if new_word in once:
            once.remove(new_word)
            answers.add(new_word)
        else:
            once.add(new_word)
        
    return list(answers)

# Test
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print repeated_substrings(s)
