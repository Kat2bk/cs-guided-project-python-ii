"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

def get_count(input_str):
    lowercase = input_str.lower()
    vowelCount = 0
    vowels_list = ["a", "e", "i", "o", "u"]
    for i in lowercase:
        if i in vowels_list:
            vowelCount += 1
    return vowelCount

print(get_count("Hello, my name is Katherine"))
print(get_count("I'm a slow learner, but I do learn"))


