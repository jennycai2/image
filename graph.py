# graph

# min cut ###########################################################
file1 = '/Users/jenny/Downloads/KargerMinCut.txt'

def get_array(filename):
    text_file = open(filename, "r")
    arry = text_file.readlines()
    #print lines
    print len(arry)
    text_file.close()

    return arry

arry = get_array(file1)

def count_edges(arry):
    cnt = 0
    for i in range(len(arry)):
        cnt += (len(arry[i]) - 1)
    return cnt/2

print count_edges(arry)  #9185

# 4 vertices
# 1, 2, 3, 4
v = [[1,2,3,4],[2,1,4],[3,1,4],[4,1,2,3]]

def add_cost(arry):
    vnew=[]
    for i in range(len(arry)):
        vc = [arry[i][0]]
        for j in range(1, len(arry[i])):
            vc.append(arry[i][j])
            vc.append(1)
        vnew.append(vc)
    return vnew

def remove_one_edge(vector, b):
    vec = []
    for i in range(len(vector)/2):
        if vector[2*i] != b:
            vec.append(vector[2*i])
            vec.append(vector[2*i+1])
    return vec

def merge_a_b(vec_a, vec_b):
    for i in range(len(vec_b)/2):
        updated = False
        for j in range(len(vec_a)/2):

            if vec_b[2*i] == vec_a[2*j]:
                vec_a[2*j+1] += vec_b[2*i+1]
                updated = True
        if (updated == False):
            vec_a.append(vec_b[2*i])
            vec_a.append(vec_b[2*i+1])

    return vec_a

def consolidate(vector, a, b):
    vec = []
    tmp = []
    for i in range(len(vector)/2):
        if vector[2*i] != b:
            vec.append(vector[2*i])
            vec.append(vector[2*i+1])
        else:
            tmp = [a, vector[2*i+1]]
    return merge_a_b(vec, tmp)

def merge_two_nodes(arry, a, b):
    # remove node b
    arr = []
    vec_a = []
    vec_b = []
    for i in range(len(arry)):

        if arry[i][0] == a:
            # remove its connection to b if it exists
            vec_a = arry[i][1:]
            vec_a = remove_one_edge(vec_a, b)
        elif arry[i][0] == b:
            # remove its connection to a if it exists; for all other
            # connections, add them to a
            vec_b = arry[i][1:]
            vec_b = remove_one_edge(vec_b, a)
        else:
            # if a connection is to b, change it to a
            tmp = [arry[i][0]] + consolidate(arry[i][1:], a, b)
            arr.append(tmp)

    vec_ab = merge_a_b(vec_a, vec_b)
    tmp = [a] + vec_ab
    arr.append(tmp)
    return arr

v1 = add_cost(v)

v2 = merge_two_nodes(v1, 1, 2)
v3 = merge_two_nodes(v2, 1, 3)
print v3
