# Given a list of lists, return a list after removing all nested lists

def flatten_list(input_list):
    output_list = []
    
    for element in input_list:
        # checking for list type
        if type(element) == list:
            # calling the same function with current element as new argument
            output_list += (flatten_list(element))
        else:
            output_list.append(element)

    return output_list


def test(got, expected):
    if got == expected:
        prefix = ' OK - '
    else:
        prefix = '  X - '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


test(flatten_list([1,2,[3,4,[5,6]], 7]), [1,2,3,4,5,6,7])
test(flatten_list([[],[[]]]), [])
test(flatten_list([[[1]]]), [1])
test(flatten_list([[100,99], [1,2,3], []]), [100,99,1,2,3])