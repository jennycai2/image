
# two words are anagrams if they have the same letters, in a different order

# cat, act
# rats, arts
# dog, god
# add, dad

# find_anagrams function
# INPUT:
# OUTPUT: ['rats', 'arts', 'star', 'dog', 'god']
#     Return a list of the strings from the input list that are anagrams with another
#     string in the input list.

word_list = ['cat', 'rats', 'dog', 'god', 'car', 'arts', 'star']
def anagrams(list1):
    big_dict = {}
    for wd in list1:
        # separate a word into letters and sort the letters
        list11 = []
        for i in range(len(wd)):
            list11.append(wd[i])
        big_dict[wd] = tuple(sorted(list11))

   # need to reverse the entries in big_dict
    reverse_dict = {}
    result = []
    for key1 in big_dict:
       value = big_dict[key1]
       if value in reverse_dict:
          # now value becomes key
          reverse_dict[value] += (' ' + key1)
       else:
          reverse_dict[value] = key1

    for key2 in reverse_dict:
       words = reverse_dict[key2].split(' ')
       if len (words) != 1: # find anagrams
          result += words
    return result


print anagrams(word_list)
