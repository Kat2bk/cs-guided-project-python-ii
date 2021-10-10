"""
Challenge #3:

Given a string of numbers separated by a comma and space, return the product of the numbers.

Examples:
- multiply_nums("2, 3") ➞ 6
- multiply_nums("1, 2, 3, 4") ➞ 24
- multiply_nums("54, 75, 453, 0") ➞ 0
- multiply_nums("10, -2") ➞ -20

Notes:
- Bonus: Try to complete this challenge in one line!
"""
# need to turn into integers
# probably need to loop through and convert to a list of integers
# while returning the product
# split?

def multiply_nums(nums):
    convertNum = nums.split(', ')
    # integers = [int(i) for i in convertNum]
    # result = 1
    # for x in integers:
    #     result = result * x
    # return result
    nums = list(map(int, convertNum))
    # you can loop through the map and apply the product to it

print(multiply_nums("2, 3"))
print(multiply_nums("1, 2, 3, 4"))
print(multiply_nums("54, 75, 453, 0"))
print(multiply_nums("10, -2"))

