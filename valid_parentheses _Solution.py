# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#   1. Open brackets must be closed by the same type of brackets.
#   2. Open brackets must be closed in the correct order.


def valid_parentheses(s):
    queue = []
    parn_dict = {"{": "}", "(": ")", "[": "]"}

    for par in s:
        if par in parn_dict:
            queue.append(par)
        # if string starts with closing parentheses
        elif len(queue) == 0:
            return False
        # compare closing parantheses with the last open one
        elif parn_dict[queue.pop()] !=  par:
            return False
    
    return True


def test(got, expected):
    if got == expected:
        prefix = ' OK - '
    else:
        prefix = '  X - '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

test(valid_parentheses("()"), True)
test(valid_parentheses("()[]{}"), True)
test(valid_parentheses("(]"), False)
test(valid_parentheses("([)]"), False)
test(valid_parentheses("{[]}"), True)
test(valid_parentheses(")("), False)

