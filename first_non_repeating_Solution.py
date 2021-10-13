# Given a string 's' consisting of small english letters
# find and retrun the first non repeating char in it
# If there is no such character, return Flase
#
# fo s = "abacabad" retrun "c"

def first_non_repeating(s):
    char_histogram = {}

    for char in s:
        if char not in char_histogram:
            char_histogram[char] = 1
        else:
            char_histogram[char] += 1

    for char in s:
        if char_histogram[char] == 1:
            return(char)

    return(False)

def test(got, expected):
    if got == expected:
        prefix = ' OK - '
    else:
        prefix = '  X - '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


test(first_non_repeating('abacabad'), 'c')
test(first_non_repeating('abacdabcd'), False)
