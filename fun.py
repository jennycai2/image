# for fun
# given the upper left corner x and y coordinates, the width, the height of 2 rectangles
# returns 'true' if the rectangles overlap
def in_range(p, left, right):
    if p >= left and p<= right:
        return True
    return False

def overlap(r1, r2):
    x1, y1, width1, height1 = r1
    x2, y2, width2, height2 = r2

    if (in_range(x2, x1, x1 + width1) or in_range(x2+width2, x1, x1+width1)) \
    and (in_range(y2, y1, y1 + height1) or in_range(y2+height2, y1, y1+height1)):
        return True

    return False

rec1 = (3,6,3,1)
rec2 = (4,7,1,3)
rec3 = (100,100,1,1)
print overlap(rec1, rec2)
print overlap(rec1, rec3)


"""
Problem: You are given a character array like "d3b1c1d1e4f0g11".
You need to expand the array by repeating the characters preceding each of the numbers.
For example, the above character array expands to "dddbcdeeeeggggggggggg".
"""

def get_letter(string1):
    ll = '0' # indicate an error
    if string1 != []:
        ll = string1[0]
        string1 = string1[1:]
        #print string1
    return ll, string1

def get_letter_indx(string1):
    for i in range(len(string1)):
        if string1[i].isalpha():
            return i
    return len(string1)

def get_number(string1):
    nn = 0
    nn_str = []
    if string1 != []:
        indx = get_letter_indx(string1)
        nn = int(string1[0:indx])
        if indx == len(string1):
            string1 = []
        else:
            string1 = string1[indx:]

    return nn, string1

def expand(string1):
    string2 = ''
    while (string1!=[]):
        letter, string1 = get_letter(string1)
        print letter, string1
        num, string1 = get_number(string1)
        print num, string1
        for i in range(num):
            string2 += letter
    return string2

string2 = expand('d3b1c1d1e4f0g11')
if string2 == 'dddbcdeeeeggggggggggg':
    print 'correct'
