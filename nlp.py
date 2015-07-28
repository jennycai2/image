# NLP

import math

D1 = "Data scientists process data and build models."
D2 = 'IOS engineers build apps.'
D3 = 'Data engineers prepare data.'

stop_words = ['and', 'the', 'a', 'an']

def is_stop_word(wd):
    for i in range(len(stop_words)):
        if wd == stop_words[i]:
            return True
    return False

def process(docu):
    # usually we use regular expression to remove punctuations
    if docu[-1]=='.':
        docu = docu[:-1]
    docu = docu.lower()
    tokens = docu.split(' ')
    # remove stop words
    new_tokens = []
    for i in range(len(tokens)):
        if is_stop_word(tokens[i]) == False:
            new_tokens.append(tokens[i])
   # need to change words to their common stem, such as apps to app
    #print new_tokens
    return new_tokens
#process(D1)

def compute_tf(docu):
    n = len(docu)
    dict1 = {}
    for i in range(n):
        if docu[i] not in dict1:
            dict1[docu[i]] = 1.0/n
        else:
            dict1[docu[i]] = (dict1[docu[i]] * n + 1.0)/n
    return dict1
#print compute_tf(['data', 'scientists', 'process', 'data'])

def build_idf(vocab, docum):
    d = len(vocab)
    n = len(docum)
    token_and_idf = {}
    for i in range(d):
        cnt = 0
        for j in range(n):
            if vocab[i] in docum[j]:
                cnt += 1
        if cnt != 0:
            idf = float(n) / cnt   # n is total number of documents
        else:
            idf = -1.0
        token_and_idf[vocab[i]] = idf
    return token_and_idf


def compute_weight(ordered_vocab, idf, docu):
    vec = [0.0]*len(ordered_vocab)

    tf = compute_tf(docu)
    print 'tf', tf

    for i in range(len(docu)):
        tf1 = 0.0
        idf1 = 0.0
        if docu[i] in tf:
            tf1 = tf[docu[i]]
        if docu[i] in idf:
            idf1 = idf[docu[i]]
        idx = ordered_vocab.index(docu[i])
        vec[idx] = tf1 * idf1
        #print docu[i], tf1, idf1
    return vec

def build_matrix(data):
    n = len(data)
    docum = []
    for i in range(n):
        docum.append(process(data[i]))
    print docum
    flat_list = [item for sublist in docum for item in sublist]

    vocab = list(set(flat_list))
    print vocab, len(vocab)

    idf = build_idf(vocab, docum)
    print 'idf', idf

    matr = []
    ordered_vocab = list(idf)
    for i in range(n):
        vec = compute_weight(ordered_vocab, idf, docum[i])
        matr.append(vec)
    print docum
    print matr[0]
    print matr[1]
    print matr[2]
    return matr


data = [D1, D2, D3]
build_matrix(data)
