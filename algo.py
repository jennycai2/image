import os




# TwoSum, count the number of triples in a file of N integers that sum to 0

a = [1,2,3, -1, -2, -3]
b =[-3,-2,-1,0,1,2,3]


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

def ThreeSum(arr):
    cnt = 0
    #print "len of array"
    #print len(arr)
    for i in range (0, len(arr)):
        cnt += CntTwoSum(arr[(i+1):], 0-arr[i])
        print i, cnt

    return cnt


print ThreeSum(a)
print ThreeSum(b)
