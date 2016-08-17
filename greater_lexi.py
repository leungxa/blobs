# Given a word , rearrange the letters of  to construct another word
# in such a way that  is lexicographically greater than . In case of
# multiple possible answers, find the lexicographically smallest one
# among them.

def _solve(string):
    head = string[0]
    tail = string[1:]
    
    new_head = tail[0]
    found_i = 0
    for i, char in enumerate(tail):
        if char > head and char < new_head:
            new_head = char
            found_i = i
    new_tail = tail[:found_i] + head + tail[found_i+1:]
    # print "new_tail", new_tail
    # print "new_head", new_head
    return new_head + ''.join(sorted(new_tail))

    
def greater_string(string):
    i = len(string) - 1
    while (i > -1):
        if (i > 0 and string[i] > string[i-1]):
            first = string[:i-1]
            second = string[i-1:]
            print "solving", second, "solved", _solve(second)
            return first + _solve(second)
        elif (i == 0):
            return 'No answer'
        i -= 1

print greater_string('') == 'No answer'
print greater_string('bb') == 'No answer'
print greater_string('hefg') == 'hegf'
print greater_string('dhck') == 'dhkc'
print greater_string('dkhc') == 'hcdk'
print greater_string('fgkhag') == 'fgkhga'
print greater_string('fgkhae') == 'fgkhea'
print greater_string('fgkhea') == 'fhaegk'
print greater_string('fgkheaaklsjdflkajsdlfkjalksdjflkajsdlfkjaksldjflakjsdflkajlksjlfaksjae') == 'fgkheaaklsjdflkajsdlfkjalksdjflkajsdlfkjaksldjflakjsdflkajlksjlfaksjea'