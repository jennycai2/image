# statistics


# a medicine cures 90% of patients. Is it true?
# or a loaded coin with p(Heads) = 0.9
# treat n patients
# flip the coin n times
# (n+1) outcomes, with the heads showing up 0, 1, 2,..., or n times


def compute_combination(n, x):
    # how many ways to take 2 out of 5
    # it's 5*4 / 2*1
    res = 1
    for i in range (x):
        res *= (n-i)
    for i in range(x):
        res = res/(i+1)
    #print res
    return res

# showing up x times
def compute_prob(n, p, x):
    return p**x * (1-p)**(n-x) * compute_combination(n, x)

# sanity check
def compute_total(n, p):
    total = 0.0
    for i in range(n+1):
        total += compute_prob(n, p, i)

    if total != 1.0:
        print 'error'
    return total
#print compute_total(15, 0.9)

def compute_combined_prob(n, p, m1, m2):
    # show up more than m times
    total = 0.0
    for i in range(m1, m2+1):
        total += compute_prob(n, p, i)
        #print n,p,m1,m2,total
    return total
#compute_combined_prob(15, 0.9, 0, 11)

def compute_pvalue(n, p, m):
    return compute_combined_prob(n,p,0,m)

for i in range(16):
    print 'xxx', i, compute_pvalue(15, 0.9, i)

def compute_num_from_pvalue(n, p, alpha=0.05):
    # find the max value that is < alpha
    # suppose m2 = 0, 1, 2 all < alpha, return 2
    find_the_value = False
    m2 = 0
    saved_pvalue = 0.0

    for i in range(n+1):
        pvalue = compute_pvalue(n, p, i)
        print 'yyy', i, pvalue
        if pvalue < alpha:
            find_the_value = True
            m2 = i
            saved_pvalue = pvalue
    if find_the_value == True:
        return m2, saved_pvalue
    return -1, 0

num, pvalue = compute_num_from_pvalue(15, 0.9)
print 'if the number is <= ', num, "pvalue is ", pvalue, "we should reject"
