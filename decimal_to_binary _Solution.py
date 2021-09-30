# Given a positive decimal, retrun its binary representation

def decimal_to_binary(number):
    div, mod = 0,0
    bin_number = ''
    
    if number == 0:
        return 0

    while number > 0:
        div = number // 2
        mod = number % 2

        number = div
        bin_number = str(mod) + bin_number

    return(bin_number)


def test(got, expected):
    if got == expected:
        prefix = ' OK - '
    else:
        prefix = '  X - '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

test(decimal_to_binary(5), '101')
test(decimal_to_binary(7), '111')
test(decimal_to_binary(10), '1010')