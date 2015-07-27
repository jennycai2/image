# K means
import math

def distance(pt1, pt2):
    d = len(pt1)
    summ = 0
    for i in range(d):
        summ += (pt1[i] - pt2[i])**2
    return summ
#print distance([1,1,1], [2,3,4])

def near_which_centeroid(element, centre, k):
    min_diff = 0
    indx = 0
    for i in range(k):
        diff = distance(element, centre[i])
        if (min_diff == 0):
            min_diff = diff # set baseline for max_diff
        if diff < min_diff:
            min_diff = diff
            indx = i
    return indx
#print near_which_centeroid([0,0,0], [[-5,-5,-5],[10,10,10]], 2)

def compute_centroids(points, d):
    summ=[0.]*d

    n1 = len(points)
    if n1==0:
        return summ

    for i in range(n1):
        for j in range(d):
            summ[j] += points[i][j]
    for j in range(d):
        summ[j] = summ[j] / n1
    return summ

def compute_variance(points, centro):
    n1 = len(points)
    summ = 0.0
    for i in range(n1):
        summ += distance(points[i], centro)

    return summ/(n1)  # can't use (n1-1) since we may have only one point

# points has n elements, each element is d-dimension
def kmeans(points, k):
    # pick some centeroids
    n = len(points)
    d = len(points[0])
    elem = [0.]*d
    centro = []
    variance1 = []
    if (k<=0):
        k=1
    if (k > n):  # at most, we can divide into n groups
        k=n

    groups = [None]*k
    # use the initial k points as the centeroids
    for i in range(k):
        centro.append(points[i])
        variance1.append(0.)
        groups[i] = []
    # assume each element is associated with centroid 0
    indx_arr = [0]*n
    for i in range(n):
        groups[0].append(points[i])
    change = True
    iter_times = 0

    while (change and iter_times< 1000):
        change = False
        iter_times += 1
        for i in range(n):
            indx = near_which_centeroid(points[i], centro, k)
            if points[i] not in groups[indx]:
                change = True
                groups[indx].append(points[i])
                if points[i] in groups[indx_arr[i]]:
                    groups[indx_arr[i]].remove(points[i])
                indx_arr[i] = indx

        print 'iter_times', iter_times, 'indx_arr', indx_arr
        print 'groups[0]', groups[0]
        for i in range(k):
            centro[i] = compute_centroids(groups[i], d)
            variance1[i] = compute_variance(groups[i], centro[i])

        average1 = sum(variance1)/len(variance1)
        print 'centro', centro, 'variance1', variance1, 'average1', average1, 'change', change
    return centro, average1

A = [[1,0],[2,0],[3,0], [0,10], [0, 11]]
B = [[1,0],[2,0],[3,0], [0,10], [0, 11],[100,100]]
elem = B

for i in range(1, len(elem)+1):
    centro, average1 = kmeans(elem, i)
    print 'xxxxxxxx', i, average1
# python kmeans.py | grep xxx
# when k increases, average1 decreases very little, that's the right value of k


#new_elem = [0,12]
#print near_which_centeroid(new_elem, model, len(model))
