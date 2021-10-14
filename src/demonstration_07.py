"""
Challenge #7:

Given a string of lowercase and uppercase alpha characters, write a function
that returns a string where each character repeats in an increasing pattern,
starting at 1. Each character repetition starts with a capital letter and the
rest of the repeated characters are lowercase. Each repetition segment is
separated by a `-` character.

Examples:
- repeat_it("abcd") -> "A-Bb-Ccc-Dddd"
- repeat_it("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
- repeat_it("cwAt") -> "C-Ww-Aaa-Tttt"
"""

# going to need to use the index to increase by its value to element

# key words: repeat(), replace(), .split()
# we need to split the letters
# for loop, repeat by index + 1, replace space with dashes
# we have to change string into int then add by index

["abcd"]
["a", "b", "c", "d"]
["a", "bb", "ccc", "dddd"]
# [0] [1] [2] [3]

def repeat_it(input_str):
    splitLst = list(input_str)
    loopingIdx = [splitLst[idx] * (idx + 1) for idx, ele in enumerate(splitLst)]
    replaceList = [i.capitalize() for i in loopingIdx]
    result = "-".join(replaceList)
    return result

print(repeat_it("abcd"))
