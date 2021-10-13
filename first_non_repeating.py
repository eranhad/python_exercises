# Given a string 's' consisting of small english letters
# find and retrun the first non repeating char in it
# If there is no such character, return Flase
#
# fo s = "abacabad" retrun "c"

def first_non_repeating(s):
# Enter code here

def test(got, expected):
    if got == expected:
        prefix = ' OK - '
    else:
        prefix = '  X - '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


test(first_non_repeating('abacabad'), 'c')
test(first_non_repeating('abacdabcd'), False)
