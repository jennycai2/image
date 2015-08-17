# graph

# min cut ###########################################################
file1 = '/Users/jenny/Downloads/KargerMinCut.txt'

def get_array(filename):
    text_file = open(filename, "r")
    arr = text_file.readlines()
    text_file.close()
    arry = []
    for i in range(len(arr)):
        tok = arr[i].split('\t')
        vec = []
        for j in range(len(tok)-1): # the last one is '\r\n'
            vec.append(int ( tok[j] ) )
        arry.append(vec)
    return arry

def get_vector_edges(vec):
    edges = []
    node0 = vec[0]
    for i in range(1, len(vec)):
        if node0 < vec[i]:
            edges.append([node0, vec[i]])
    return edges

def get_edges(arry):
    edges = []
    for i in range(len(arry)):
        edges += get_vector_edges(arry[i])
    return edges

def count_edges(arry):
    cnt = 0
    for i in range(len(arry)):
        cnt += (len(arry[i]) - 1)
    return cnt/2

def remove_one_edge(one_edge, edges):
    #print 'one_edge', one_edge, len(edges)
    kept_edges = []
    for i in range(len(edges)):
        if edges[i] != one_edge:
            kept_edges.append(edges[i])
    #print 'xx,', len(kept_edges)
    return kept_edges

def get_one_edge(edges):
    one_edge = []
    if len(edges) > 1:
        one_edge = edges[0]
        edges = remove_one_edge(one_edge, edges)
    #print 'xxx', one_edge, edges
    return one_edge, edges

def contain_this_edge(one_edge, edges):
    for i in range(len(edges)):
        if one_edge == edges[i]:
            return True
    return False

def add_edges_if_not_dup(node0_edges, edges):
    for i in range(len(node0_edges)):
        if contain_this_edge(node0_edges[i], edges) == False:
            edges.append(node0_edges[i])
            #print 'add the converted edge', node0_edges[i]
    return edges

def convert_then_check_edges(removed_edge, edges):
    node0 = removed_edge[0]
    node1 = removed_edge[1]

    node0_edges = []
    conv_edges = []
    for i in range(len(edges)):
        if edges[i][0] == node1:
            # convert an edge with node1 to node0, and smaller number first
            node0_edges.append(sorted([node0, edges[i][1]]))
        elif edges[i][1] == node1:
            # convert an edge with node1 to node0, and smaller number first
            node0_edges.append(sorted([node0, edges[i][0]]))
        else:
            conv_edges.append(edges[i])
    conv_edges = add_edges_if_not_dup(node0_edges, conv_edges)
    #print conv_edges
    return conv_edges

def add_cost(arry):
    arr_new=[]
    for i in range(len(arry)):
        vec = [arry[i][0]]
        for j in range(1, len(arry[i])):
            vec.append(arry[i][j])
            vec.append(1)
        arr_new.append(vec)
    return arr_new

def remove_two_nodes(vector, b):
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
            vec_a = remove_two_nodes(vec_a, b)
        elif arry[i][0] == b:
            # remove its connection to a if it exists; for all other
            # connections, add them to a
            vec_b = arry[i][1:]
            vec_b = remove_two_nodes(vec_b, a)
        else:
            # if a connection is to b, change it to a
            tmp = [arry[i][0]] + consolidate(arry[i][1:], a, b)
            arr.append(tmp)

    vec_ab = merge_a_b(vec_a, vec_b)
    tmp = [a] + vec_ab
    arr.append(tmp)
    return arr

# 4 vertices
# 1, 2, 3, 4
v00 = [[1,2,3,4],[2,1,4],[3,1,4],[4,1,2,3]]
v1 = add_cost(v00)
v2 = merge_two_nodes(v1, 1, 2)
v3 = merge_two_nodes(v2, 1, 3)

v01 = [[1,2,7,8],[2,1,8,7,3],[3,2,6,5,4],[4,3,6,5],[5,4,3,6],[6,7,3,4,5],[7,2,6,1,8],[8,1,2,7]]
v1 = add_cost(v01)
v2 = merge_two_nodes(v1, 1, 2)
v3 = merge_two_nodes(v2, 1, 7)
v4 = merge_two_nodes(v3, 1, 8)
v5 = merge_two_nodes(v4, 3, 4)
v6 = merge_two_nodes(v5, 3, 5)
v7 = merge_two_nodes(v6, 3, 6)
#print v7

arry = get_array(file1)
print 'number of edges', count_edges(arry)  #2517
edges = get_edges(arry)
#print 'edges', edges
vertices_arr = add_cost(arry)
print 'number of nodes', len(vertices_arr)
cnt = 0
prev_edge_num = len(edges)
one_edge, edges = get_one_edge(edges)
#print one_edge
#print edges
while (one_edge!=[] and cnt < 2517):
    cnt += 1
    print "iteration ", cnt
    edges = convert_then_check_edges(one_edge, edges)
    #print "after converting", edges, "edges have decreased ", prev_edge_num - len(edges), " to ", len(edges)
    node0 = one_edge[0]
    node1 = one_edge[1]
    vertices_arr = merge_two_nodes(vertices_arr, node0, node1)

    # sanity check
    cnt1 = count_edges(vertices_arr) / 2 # ignore the cost elements
    cnt2 = len(edges)
    if cnt1 != cnt2:
        print "Not equal!"
    #print "cnt from vertices", cnt1, "cnt from edges", cnt2

    prev_edge_num = len(edges)
    one_edge, edges = get_one_edge(edges)
    #print '\n\n', one_edge
    #print edges

#print v1
