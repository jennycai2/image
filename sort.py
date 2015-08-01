# merge sort

arr0 = [4, 2]

arr1 = [2,5, 7, 9]
arr2 = [1,8,9]

arr3 = [2,5, 7, 9, 1, 8, 9]

arr4 = [2, 4, 1, 3, 9]

def num_of_inversions(arr1):
    cnt = 0
    n = len(arr1)
    if n<2:
        return 0
    for i in range(n-1):
        if arr1[i] > arr1[i+1]:
            cnt += 1
    return cnt

def merge_two_sorted_lists(arr1, arr2):
    n = len(arr1) + len(arr2)
    arr0 = []

    i = 0
    j = 0
    for k in range(n-1):
        if arr1[i] < arr2[j]:
            arr0.append(arr1[i])
            i += 1
        else:
            arr0.append(arr2[j])
            j += 1
        #print 'k', k, 'i', i, 'j', j, 'arr0', arr0

    # the last element can't use the above comparison, since it's out of range
    if i<len(arr1):
        arr0.append(arr1[i])
    else:
        arr0.append(arr2[j])

    return arr0


def find_insert_posi(arr1, elem, beginning_indx):
    for i in range(beginning_indx, len(arr1)):
        if elem <= arr1[i]:
            return i

    return len(arr1)

def old_merge_two_sorted_lists(arr1, arr2):
    # which vector is shorter?

    updated_arr = arr1
    indx = 0
    for i in range(len(arr2)):
        indx = find_insert_posi(updated_arr, arr2[i], indx)
        #print indx
        updated_arr = updated_arr[:indx] + [arr2[i]] + updated_arr[indx:]
        #print updated_arr[:indx], [arr2[i]], updated_arr[indx:]
    return updated_arr

def merge_sort(arr1):
    n = len(arr1)
    arr0 = arr1[0:n/2]
    arr2 = arr1[n/2:]
    return merge_two_sorted_lists(arr0, arr2)

print merge_sort(arr4)
