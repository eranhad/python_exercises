# Complete a function that returns the number of times a given character occurs in the given string.
# For example:
# - input string = "mississippi"
# - char = "s"
# - output : 4

def char_occurrence_in_string(word, char):
    i = 0
    
    for letter in word:
        if char == letter:
            i += 1
    
    return(i)

def test(got, expected):
    if got == expected:
        prefix = ' OK - '
    else:
        prefix = '  X - '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

test(char_occurrence_in_string("mississippi", "s"), 4)