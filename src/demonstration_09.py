"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"

# finding the middle means looping through
# the middle of something is half, probably divide the list by length // 2
# if len(input_str % 2) == 0 return  
# edge cases: if nothing is in the string, if the string is a single word, one letter

"""
def get_middle(input_str):
    if len(input_str) == 0:
        return ""
    elif len(input_str) % 2 == 0:
        return input_str[len(input_str) // 2 - 1] + input_str[len(input_str) // 2]
    elif len(input_str) % 2 != 0:
        return input_str[len(input_str) // 2]


print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(("A"))
