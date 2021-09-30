# Given a positive decimal, retrun its binary representation

def decimal_to_binary(number):
# Enter code here


def test(got, expected):
    if got == expected:
        prefix = ' OK - '
    else:
        prefix = '  X - '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

test(decimal_to_binary(5), '101')
test(decimal_to_binary(7), '111')
test(decimal_to_binary(10), '1010')