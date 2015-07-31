# merge sort

arr1 = [2,5, 7, 9]
arr2 = [1,8,9]


def find_insert_posi(arr1, elem, beginning_indx):
    for i in range(beginning_indx, len(arr1)):
        if elem <= arr1[i]:
            return i

    return len(arr1)

def merge_sort(arr1, arr2):
    # which vector is shorter?

    updated_arr = arr1
    indx = 0
    for i in range(len(arr2)):
        indx = find_insert_posi(updated_arr, arr2[i], indx)
        print indx
        updated_arr = updated_arr[:indx] + [arr2[i]] + updated_arr[indx:]
        print updated_arr[:indx], [arr2[i]], updated_arr[indx:]
    return updated_arr


a = merge_sort(arr1, arr2)
print a
