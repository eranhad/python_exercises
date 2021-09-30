# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#   1. Open brackets must be closed by the same type of brackets.
#   2. Open brackets must be closed in the correct order.


def valid_parentheses(s):
# Enter code here


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

