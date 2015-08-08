# merge sort

arr0 = []
arr1 = [1]
arr2 = [4, 2]
arr3 = [1,8,9]
arr4 = [1,3, 2, 4]
arr5 = [2, 4, 1, 3, 9]
arr6 = [1, 3, 5, 2, 4, 6]
arr7 = [2,5, 7, 9, 1, 8, 9]
global_cnt = 0


def quicksort(arr0):
    n = len(arr0)
    if n<=1:
        return arr0
    arr1=[]
    arr2=[]
    p = arr0[0]
    for i in range(1, n):
        if arr0[i] < p:
           arr1.append(arr0[i])
        else:
           arr2.append(arr0[i])
    #print 'arr1, arr2', arr1, arr2
    return quicksort(arr1) + [p] + quicksort(arr2)


q = quicksort(arr7)
print q

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

#print threeWaySort(arr7)
def merge_and_countSplitInv(arr1, arr2):
    print 'arr1, arr2', arr1, arr2
    n = len(arr1) + len(arr2)
    arr0 = []
    cnt = 0

    i = 0
    j = 0
    for k in range(n-1):
        if arr1[i] <= arr2[j]:
            arr0.append(arr1[i])
            i += 1
            if i== len(arr1):
                #print "wow, i is at max"
                arr0.extend(arr2[j:])
                return cnt, arr0
        else:
            arr0.append(arr2[j])
            j += 1
            cnt += (len(arr1) - i)
            print 'cnt', cnt
            if j== len(arr2):
                #print "wow, j is at max"
                arr0.extend(arr1[i:])
                return cnt, arr0
        #print 'k', k, 'i', i, 'j', j, 'arr0', arr0

    return cnt, arr0


def sort_and_count(arr1):
    cnt = 0
    n = len(arr1)
    if n<2:
        return cnt, arr1
    arr0 = arr1[0:n/2]
    arr2 = arr1[n/2:]
    cnt, arr0 = sort_and_count(arr0)
    #global_cnt += cnt
    cnt, arr2 = sort_and_count(arr2)
    #global_cnt += cnt
    return merge_and_countSplitInv(arr0, arr2)

print 'arr', arr2
cnt, arr0 = sort_and_count(arr2)
#cnt, arr0 = sort_and_count(arr4)
#cnt, arr0 = sort_and_count(arr6)
