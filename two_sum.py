# Given an array of integer nums and an integer target, 
# return the two numbers such that they add up to target.

def two_sum(numbers, target):
# Enter code here


def test(got, expected):
    if got == expected:
        prefix = ' OK - '
    else:
        prefix = '  X - '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


test(two_sum([2,7,11,15], 9), [2, 7])
test(two_sum([3,2,4], 6), [2, 4])
test(two_sum([3,3], 6), [3,3])
test(two_sum([1,5,7], 9), None)