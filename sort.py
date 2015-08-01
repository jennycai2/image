# merge sort

arr0 = []
arr1 = [1]
arr2 = [4, 2]
arr3 = [1,8,9]
arr4 = [2,5, 7, 9]
arr5 = [2, 4, 1, 3, 9]
arr6 = [2, 4, 1, 3, 9, 10]
arr7 = [2,5, 7, 9, 1, 8, 9]

def num_of_inversions(arr1):
    cnt = 0
    n = len(arr1)
    if n<2:
        return 0
    for i in range(n-1):
        if arr1[i] > arr1[i+1]:
            cnt += 1
    return cnt


def merge(arr1, arr2):
    print 'arr1, arr2', arr1, arr2
    n = len(arr1) + len(arr2)
    arr0 = []

    i = 0
    j = 0
    for k in range(n-1):
        if arr1[i] <= arr2[j]:
            arr0.append(arr1[i])
            i += 1
            if i== len(arr1):
                #print "wow, i is at max"
                arr0.extend(arr2[j:])
                return arr0
        else:
            arr0.append(arr2[j])
            j += 1
            if j== len(arr2):
                #print "wow, j is at max"
                arr0.extend(arr1[i:])
                return arr0
        #print 'k', k, 'i', i, 'j', j, 'arr0', arr0

    return arr0

def sort(arr1):
    #print 'arr1', arr1
    n = len(arr1)
    if n<2:
        return arr1
    arr0 = arr1[0:n/2]
    arr2 = arr1[n/2:]
    arr0 = sort(arr0)
    arr2 = sort(arr2)
    return merge(arr0, arr2)

#print sort(arr7)

def threeWayMerge(arr1, arr2, arr3):
    print 'arr1, arr2, arr3', arr1, arr2, arr3

    arr12 = merge(arr1, arr2)
    return merge(arr12, arr3)

def threeWaySort(arr1):
    #print 'arr1', arr1
    n = len(arr1)
    if n<3:
        if n<2:
            return arr1
        else:
            if arr1[0] <= arr1[1]:
                return arr1
            else:
                return [arr1[1], arr1[0]]
    arr0 = arr1[0:n/3]
    arr2 = arr1[n/3:n*2/3]
    arr4 = arr1[n*2/3:]
    arr0 = threeWaySort(arr0)
    arr2 = threeWaySort(arr2)
    arr4 = threeWaySort(arr4)
    return threeWayMerge(arr0, arr2, arr4)
print threeWaySort(arr7)
