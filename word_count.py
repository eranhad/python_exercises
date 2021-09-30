# Return the number of words from the input string

def word_count(input_str):
    list_of_words = input_str.split()
    
    return len(list_of_words)


def test(got, expected):
    if got == expected:
        prefix = ' OK - '
    else:
        prefix = '  X - '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

test(word_count(''), 0)
test(word_count('Hello World'), 2)
test(word_count('Hello Hello'), 2)
test(word_count('Good Morning America'), 3)
test(word_count('   connect the   world together '), 4)