# In a string detect the smallest window length with highest number of distinct characters. For eg.
# A = “aabcbcdbca”, then ans would be 4 as of “dbca”

def distinct_substring(input):
    seen = set()
    longest = ''
    start_pos = 0
    current = ''

    for x in range(0, len(input)):
        char = input[x]
        if char not in seen:
            seen.add(char)
        else:
            jump = 1
            for x in range(0, len(current)):
                if current[x] != char:
                    jump += 1
                    seen.remove(current[x])
                else:
                    break
            start_pos += jump
            if len(current) > len(longest):
                longest = current
            current = current[x+1:]
        current += char
    return longest if len(longest) > len(current) else current

def dumb_distinct(input):
    longest = ''
    for start in range(0, len(input)):
        seen = set()
        for x in range(start, len(input)):
            if input[x] in seen:
                if len(input[start:x]) > len(longest):
                    longest = input[start:x]
                break
            else:
                seen.add(input[x])
                if x == len(input) - 1:
                    if len(input[start:len(input)]) > len(longest):
                        longest = input[start:len(input)]
    return longest
                

print distinct_substring('i'), dumb_distinct('i')
print distinct_substring('aaaa'), dumb_distinct('aaaa')
print distinct_substring('0123123'), dumb_distinct('0123123')
print distinct_substring('abcedfg'), dumb_distinct('abcedfg')
print distinct_substring('a01019aa08'), dumb_distinct('a01019aa08')
print distinct_substring('aabcbcdbca'), dumb_distinct('aabcbcdbca')

import timeit

def smart_tests():
#     distinct_substring('i')
#     distinct_substring('aaaa')
#     distinct_substring('0123123')
#     distinct_substring('abcedfg')
#     distinct_substring('a01019aa08')
#     distinct_substring('aabcbcdbca')
    distinct_substring('asdlfja1jofj0f9a09fja09sjf;ajlfjafjalsjjafoj0f92j30j2903fj029j309jaj ja;oj3 jaj;a lj;l2a309fja0f9j3 a90j3;aj;fja;3jfa09j099j9jjjjjjjj ;j; ja02399j09u38alhlfhalh3 a;a2j3f90j9aj3f ;aj23ofjlakjljija4nfjghkh;hauighiugailefh a2hfuk3 hihfla hfhahlkwdh fkahf lak lhfkj hasklfh72h3ua389hf ah 2a3hlf h j2ua3roh2aro 2ioa jro aj23ior jioa j3ior joia j23l rjl aj23rioja23 r89u89a2ru89ua98 jakjs hfkja hsjkfh jkah 2ui3ufh98ah898y98h98hui3fh aukh ui32h 9fha9823h89fha9823hfioahio3hfkja h3fhah23h90f8ah2389hf 98ah239 fhail3fkahklj3fh kajwh3fha23890h2890ah08fhaphfah 3fh923894729384792834798237489237498234982uy34halskjhfkjahsdklfjhas kdfajh sdfjkhaskdfhiashfiuhaw9ehf9h29fbiuasbkjf awihfh2983hfliauh3iljhaiuf huiahwfilhlaksjhfjk ha29hf98h23ufhawihf98a2y398u89478923u49283u4')

    
def dumb_tests():
#     dumb_distinct('i')
#     dumb_distinct('aaaa')
#     dumb_distinct('0123123')
#     dumb_distinct('abcedfg')
#     dumb_distinct('a01019aa08')
#     dumb_distinct('aabcbcdbca')
    dumb_distinct('asdlfja1jofj0f9a09fja09sjf;ajlfjafjalsjjafoj0f92j30j2903fj029j309jaj ja;oj3 jaj;a lj;l2a309fja0f9j3 a90j3;aj;fja;3jfa09j099j9jjjjjjjj ;j; ja02399j09u38alhlfhalh3 a;a2j3f90j9aj3f ;aj23ofjlakjljija4nfjghkh;hauighiugailefh a2hfuk3 hihfla hfhahlkwdh fkahf lak lhfkj hasklfh72h3ua389hf ah 2a3hlf h j2ua3roh2aro 2ioa jro aj23ior jioa j3ior joia j23l rjl aj23rioja23 r89u89a2ru89ua98 jakjs hfkja hsjkfh jkah 2ui3ufh98ah898y98h98hui3fh aukh ui32h 9fha9823h89fha9823hfioahio3hfkja h3fhah23h90f8ah2389hf 98ah239 fhail3fkahklj3fh kajwh3fha23890h2890ah08fhaphfah 3fh923894729384792834798237489237498234982uy34halskjhfkjahsdklfjhas kdfajh sdfjkhaskdfhiashfiuhaw9ehf9h29fbiuasbkjf awihfh2983hfliauh3iljhaiuf huiahwfilhlaksjhfjk ha29hf98h23ufhawihf98a2y398u89478923u49283u4')
    
if __name__ == '__main__':
    import timeit
    print(timeit.timeit("smart_tests()", setup="from __main__ import smart_tests", number=1000))
    print(timeit.timeit("dumb_tests()", setup="from __main__ import dumb_tests", number=1000))
