# Given a list of numbers, return dictionary with key:value of number:number of occurences in the list

def histogram(input_list):
# Enter code here


def test(got, expected):
    if got == expected:
        prefix = ' OK - '
    else:
        prefix = '  X - '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


test(histogram([2,4,1,2,3,2,1]), {2: 3, 4: 1, 1: 2, 3: 1})
test(histogram([2,1,3,4,2,4,3,4]), {2: 2, 1: 1, 3: 2, 4: 3})
test(histogram([1,2,3,4]), {1: 1, 2: 1, 3: 1, 4: 1})
test(histogram([]), {})