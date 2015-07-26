

def difference(pt1, pt2):
    d = len(pt1)
    summ = 0
    for i in range(d):
        summ += (pt1[i] - pt2[i])**2
    return summ

#print difference([1,1,1], [2,3,4])
# return an index
def nearest_centeroid(element, centre, k):
    min_diff = 0
    indx = 0
    for i in range(k):
        diff = difference(element, centre[i])
        if (min_diff == 0):
            min_diff = diff # set baseline for max_diff
        if diff < min_diff:
            min_diff = diff
            indx = i
    return indx

#print nearest_centeroid([0,0,0], [[-5,-5,-5],[10,10,10]], 2)

def add_one_element(summ, point, d):
    #for i in range(d):
    #    summ[i] += point[i]
    return summ

#summ = [0.,0.,0.]
#point=[1.,0.,0.]
#print add_one_element(summ, point, 2)

def compute_average(points):
    n1 = len(points)
    d = len(points[0])
    summ=[0.]*d
    cnt = 0
    for i in range(n1):
        cnt +=1
        for j in range(d):
            summ[j] += points[i][j]
    for j in range(d):
        summ[j] = summ[j] / cnt
    return summ

# return the centeroids, and what the point belongs to
# points has n elements, each element is d-dimension
def kmeans(points, k):
    # pick some centeroids

    n = len(points)
    d = len(points[0])

    elem = [0.]*d
    centro = []
    groups = [None]*k
    cnt = [0]*k
    summ = [elem]*k
    print 'cnt', cnt
    print 'summ', summ

    # use the initial k points as the centeroids
    for i in range(k):
        centro.append(points[i])
        groups[i] = []

    # assume each element is associated with centroid 0
    indx_arr = [0]*n

    change = True
    while (change):
     change = False
     for i in range(n):
        indx = nearest_centeroid(points[i], centro, k)
        groups[indx].append(points[i])
        indx_arr[i] = indx
        change = True
     print 'indx_arr', indx_arr

     print groups[0], groups[1]
    # compute the new centeroids
     if (change):
        for i in range(k):
            centro[i] = compute_average(groups[i])

        """
        for i in range(k):
            for j in range(n):
                if indx_arr[j] == i:
                    cnt[i] += 1
                    #print 'xxxx', summ[i], points[j]
                    #summ = add_one_element(summ[i], points[j], d)
                    #summ[i] += points[j]
        print summ


        for i in range(n):
            cnt[indx_arr[i]] += 1
            for j in range(d):
                #if (i == indx_arr[i]):
                summ[indx_arr[i]][j] += points[i][j]
                print 'update summ', indx_arr[i],j
                print 'indx_arr', indx_arr[i], 'points', points[i][j], 'summ', summ
        print 'cnt', cnt
        print 'summ', summ
        for i in range(k):
            for j in range(d):
                centro[i][j] = summ[i][j]/cnt[i]
        """
    return centro

elem = [[1,0],[2,0],[3,0], [0,10], [0, 11]]
print kmeans(elem, 2)
