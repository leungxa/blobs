"""
"hi world", "hello world" -> 4
"hi alex world", "hey tobi world" -> 6
hi         hey 3
alex       tobi 4
world      world 5

"hifalexgworld", "heyftobigworld" -> 6

i  h  i     f a l e x
i  h  e y   f a l e x

"abc" "abc" -> 0
"abc" "ac" -> 1
"ac" "abc" -> 1
"abc" "" -> 3
"" "abc" -> 3
"abc" "cde" -> 3
"""

# "abc" -> "abcabc"
# "abc" -> ""
# hillo,hello: 1

# a hillo,i hello 1 + 1 = 2

table = {}

def min_changes(string1, string2):
    if string1 == string2:
        return 0
    if (string1,string2) in table:
        return table[(string1,string2)]

    if string1 == "":
        return len(string2)
    if string2 == "":
        return len(string1)

    for i in range(len(string1)):
        pre1 = string1[i]
        pre2 = string2[0]
        if pre1 != pre2:
            minv = 1 + min(min_changes(string1[1:], string2), min_changes(string1, string2[1:]), min_changes(string1[1:], string2[1:]))
            table[(string1,string2)] = minv
            return minv
        return min_changes(string1[1:], string2[1:])

print min_changes("", "")
print min_changes("a", "b")
print min_changes("abc", "c")
print min_changes("ihifalex", "iheyfalex")
print min_changes("hi world", "hello world")
print min_changes("hi alex world", "hey tobi world")
    

   
