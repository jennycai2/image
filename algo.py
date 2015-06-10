import os
import math


# input a is number, arr is an array, a will be compared with each value in the arr
# if the sum equals to sum_value, cnt will be increased.
def TwoSum(a, arr, sum_value):
    cnt = 0
    #print "len of array"
    #print len(arr)
    for i in range (0, len(arr)):
        if a+arr[i]==sum_value:
            cnt+=1
    #print cnt
    return cnt

def CntTwoSum(arr, sum_value):
    total = 0
    for i in range (0, len(arr)):
        total += TwoSum(arr[i], arr[(i+1):], sum_value)

    return total

# ThreeSum, count the number of triples in a file of N integers that sum to 0
def ThreeSum(arr):
    cnt = 0
    #print "len of array"
    #print len(arr)
    for i in range (0, len(arr)):
        cnt += CntTwoSum(arr[(i+1):], 0-arr[i])
        print i, cnt

    return cnt


"""
code for insertion sort
"""
def find_index(arr, v):
    for i in range (0, len(arr)):
        if (v<arr[i]):
            return i
    return len(arr)

def insertion_sort(bb):
    cc = []

    if (len(bb)<=1):
        return bb

    if bb[0] > bb[1]:
        cc.append(bb[1])
        cc.append(bb[0])
    else:
        cc.append(bb[0])
        cc.append(bb[1])
    for i in range (0, len(bb)-2):
        x = find_index(cc, bb[i+2])
        cc.insert(x, bb[i+2])

    return cc

"""
code for bottom-up merge sort
"""
# for sorting 3 or more elments
def sort(arr, indx0, size):
    #arr = [1]
    #indx0 = 0
    #size = 2

    size = size/2
    indx1 = indx0 + size
    cc=arr[0:size]
    for i in range (size, len(arr)):
        x = find_index(cc, arr[i])
        cc.insert(x, arr[i])

    return cc

def merge_sort(bb):
    if (len(bb)<=1):
        return bb

    #bb = [3,1,2,0, 7,6]
    levels = math.ceil(math.log(len(bb), 2))  #ceiling (round up to next integer)
    levels = int(levels)
    #for l in range (0, levels):
    for l in range (0, 2):
        b = 2**(l+1)   # for example, at the first level, we process 2 elements
        for i in range (0, ( len(bb)+ b-1 )/b):
            #if (2*i+1) < len(bb):
            bb = sort(bb, b*i, b)
            print 'sort element ', b*i, b, bb

    return bb

a = [2,1,3, -1, -2, -3]
b =[-3,-2,-1,0,1,2,3]

print merge_sort(a)
