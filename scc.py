# compute strongly connected components

import random
import math
from collections import deque

file1 = '/Users/jenny/Downloads/SCC.txt'


undirected_list = [
[0,4,5],
[1,2,3],
[2,1,4],
[3,1,5],
[4,2,5,0],
[5,3,4,0]
]

directed_list = [
[0],
[1,2,3],
[2,4],
[3,5],
[4,5,0],
[5,0]
]

def file_to_array(filename):
    text_file = open(filename, "r")
    arr = text_file.readlines()
    text_file.close()
    arry = []
    #print len(arr)
    #print arr[len(arr)-1]
    for i in range(len(arr)):
        tok = arr[i].split(' ')
        #if i==0 or i==len(arr)-1:
        #    print tok
        vec = []
        for j in range(len(tok)-1): # the last one is '\n'
            vec.append(int ( tok[j] ) )
        arry.append(vec)
    #print len(arry)
    #print arry[len(arry)-1]
    return arry

#edges = file_to_array(file1)
#edges = edges[0:10]
#print edges

def DFS(list1, node0, result, lb):
    print '\n', node0, lb
    print result
    result[node0][0] = True # mark as visited
    sublist = list1[node0] # assume list starts from indx 0
    print sublist, len(sublist)
    n = len(sublist)
    #if (len(sublist)==1):

    for i in range(1, n):
        node1 = sublist[i]
        print i, 'node1', node1, len(sublist), n
        #if result[5][0]==False:
        if result[node1][0] == False:
            print len(result), 'xxx'
            result, lb = DFS(list1, node1, result, lb)

    result[node0][1] = lb
    lb -= 1
    return result, lb

def topological_sort(list1):
    # stack, LIFO
    # recursive
    result = []
    for i in range(len(list1)): # init for each node
        result.append([False, -1]) # not visited, topological order is -1

    lb = len(list1)  # current label

    for i in range(len(list1)):
        node = list1[i][0]
        if result[node][0] == False:
            result, lb = DFS(list1, node, result, lb)

    return result

print topological_sort(directed_list)


def scc(list1):

    return 1

# pute shortest path between s and t. We choose s as the root node
def BreadthFirstSearch(list1, s, t):
    # linear time
    # find everything you want
    # compute shortest path
    result = []
    for i in range(len(list1)): # init for each node
        result.append([False, -1]) # not visited, distance is -1

    queue = deque([s])  # init the queue with the root node
    result[s][0] = True  # so we won't enqueue it again
    result[s][1] = 0     # distance to itself is 0
    while (len(queue) != 0):
        node0 = queue.popleft()
        #print "\nNow processing node ", node0
        sublist = list1[node0] # assume list starts from indx 0
        for i in range(1, len(sublist)):
            node1 = sublist[i]
            if result[node1][0] == False: # if the node has not been enqueued, enqueue it
                queue.append(node1)
                result[node1][0] = True
                result[node1][1] = result[node0][1] + 1
    if result[t][0] == True and result[t][1] != -1:
        return result[t][1] - result[s][1]
    return -1

print BreadthFirstSearch(undirected_list, 1, 5)
