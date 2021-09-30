# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. 
# An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

def monotonic(l):
# Enter code here


def test(got, expected):
    if got == expected:
        prefix = ' OK - '
    else:
        prefix = '  X - '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

test(monotonic([1,2,5,5,8]), True)
test(monotonic([9,4,4,2,2]), True)
test(monotonic([1,4,6,3,7]), False)
test(monotonic([1,1,1,1,1]), True)