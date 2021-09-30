# Given a two dimensional list, for example [[2,3],[3,4],[5]] 
# person 2 is friends with 3 etc, There will be no duplicates such as [2,3] and [3,2]
# find how many friends each person has. 
# Note, a person can have no friends

def friends(friends_list):
    frinds_dict = {}

    for l in friends_list:
        if len(l) == 2:
            if l[0] not in frinds_dict:
                frinds_dict[l[0]] = 1
            else:
                frinds_dict[l[0]] += 1
        else:
            if l[0] not in frinds_dict:
                frinds_dict[l[0]] = 0
    
    return(frinds_dict)


def test(got, expected):
    if got == expected:
        prefix = ' OK - '
    else:
        prefix = '  X - '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

test(friends([[2,3],[3,4],[5]]), {2: 1, 3: 1, 5: 0})
test(friends([[2,3],[2,6],[5],[3,4]]), {2: 2, 5: 0, 3: 1})