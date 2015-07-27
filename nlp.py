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

def get_token_cnt(wd, docu):
    cnt = 0
    for i in range(len(docu)):
        if wd == docu[i]:
            cnt += 1
    return cnt

def get_token_vec(vocab, docu):
    vec = [0]*len(vocab)
    for i in range(len(vocab)):
        vec[i] = get_token_cnt(vocab[i], docu)
    return vec

def build_matrix(data):
    n = len(data)
    docum = []
    for i in range(n):
        docum.append(process(data[i]))
    print docum
    flat_list = [item for sublist in docum for item in sublist]
    #print flat_list
    vocab = list(set(flat_list))
    print vocab, len(vocab)

    d = len(vocab)

    matr = []
    for i in range(n):
        vec = get_token_vec(vocab, docum[i])
        matr.append(vec)
    print matr
    return matr


data = [D1, D2, D3]
build_matrix(data)
