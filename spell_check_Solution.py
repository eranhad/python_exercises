"""
Write a simple spell checking engine.
The query language is a very simple regular expression-like language, with one special character: . (the dot character), 
which means EXACTLY ONE character (it can be any character). 
So, for example, 'c.t' would match 'cat' as the dot matches any character. 
There may be any number of dot characters in the query (or none).

Your spell checker will have to be optimized for speed, so you will have to write it in the required way. 

Word List:
    [cat, bat, rat, drat, dart, drab]

Queries:
    cat -> true
    c.t -> true
    .at -> true
    ..t -> true
    d..t -> true
    dr.. -> true
    ... -> true
    .... -> true
    ..... -> false
    h.t -> false
    c. -> false

"""


def spell_check(word, input_list):
    temp_list = []

    # if the word is in the input list then return True 
    if word in input_list:
        return True

    # if word not in inlupt list and doesn't have a dot in it then return False
    elif word not in input_list and '.' not in word:
        return False

    # word has a dot in it
    else:
        for w in input_list:
            # match the words with the same length
            if len(w) == len(word):
                temp_list.append(w)
    
        for x in temp_list:
            cnt = 0
            
            # check if each letter in the word matches the letter in the word from the input list
            for i in range(len(word)):
                if (x[i] == word[i]) or (word[i]=='.'):
                    cnt += 1
                else:
                    break
                
            if cnt == len(word):
                return True

        return False
    

def test(got, expected):
    if got == expected:
        prefix = ' OK - '
    else:
        prefix = '  X - '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

test(spell_check('cat', ['cat', 'bte', 'art', 'drat', 'dart', 'drab']), True)
test(spell_check('c.t', ['cat', 'bte', 'art', 'drat', 'dart', 'drab']), True)
test(spell_check('.at', ['cat', 'bte', 'art', 'drat', 'dart', 'drab']), True)
test(spell_check('..t', ['cat', 'bte', 'art', 'drat', 'dart', 'drab']), True)
test(spell_check('d..t', ['cat', 'bte', 'art', 'drat', 'dart', 'drab']), True)
test(spell_check('dr..', ['cat', 'bte', 'art', 'drat', 'dart', 'drab']), True)
test(spell_check('...', ['cat', 'bte', 'art', 'drat', 'dart', 'drab']), True)
test(spell_check('....', ['cat', 'bte', 'art', 'drat', 'dart', 'drab']), True)
test(spell_check('.....', ['cat', 'bte', 'art', 'drat', 'dart', 'drab']), False)
test(spell_check('h.t', ['cat', 'bte', 'art', 'drat', 'dart', 'drab']), False)
test(spell_check('c.', ['cat', 'bte', 'art', 'drat', 'dart', 'drab']), False)