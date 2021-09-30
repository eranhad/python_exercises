# Delete duplicates in a list
# without turnning it into a set first!

def delete_duplicate_element(l):
# Enter code here


def test(got, expected):
    if got == expected:
        prefix = ' OK - '
    else:
        prefix = '  X - '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


test(delete_duplicate_element([]), [])
test(delete_duplicate_element([1,2,2,3]), [1,2,3])
test(delete_duplicate_element([1,1,1,1,1]), [1])
test(delete_duplicate_element([1,2,3,4,5]), [1,2,3,4,5])
test(delete_duplicate_element([1,1,2,2,3,3,4,4,5,5]), [1,2,3,4,5])