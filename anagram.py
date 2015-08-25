
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
        # each word has different letter and associated count, I'll first do that and save in a dictionary
        dict1 = {}
        for i in range(len(wd)):
            if wd[i] in dict1:
               dict1[wd[i]] += 1
            else:
               dict1[wd[i]] = 1
        print dict1
        big_dict[wd] = sorted(list(dict1))
    print big_dict
    
    list2 = list(big_dict)
   # need to reverse the entries in big_dict
   # then sort it
    reverse_dict = {}
    for key1 in big_dict:
       value = big_dict[key1]
       if value in reverse_dict:
          # now value becomes key
          reverse_dict[value] += (' ' + key1)
       else:
          reverse_dict[value] = key1
    for key2 in reverse_dict:
       words = reverse_dict[key2].split(' ')
       if len (words)   != 1: # find anagrams
          print words
    return 0


anagrams(word_list)
