# statistics

import math

from matplotlib import pyplot as plt
import scipy.stats
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

# comput binomial distribution probability
def compute_prob(n, p, x):
    return p**x * (1-p)**(n-x) * compute_combination(n, x)
#for i in range (0, 16):
#    print i, compute_prob(15, 0.9, i)
def draw_binomial_dist():
    n = 30
    p = 0.9
    xs = [x for x in range(0, n+1)]
    plt.plot(xs,[compute_prob(n, p, x) for x in xs],'-',label='mu=0,sigma=1')
    plt.plot(xs,[compute_prob(n, p, x) for x in xs],'--',label='mu=0,sigma=2')
    #plt.plot(xs,[normal_cdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
    #plt.plot(xs,[normal_cdf(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')
    plt.legend(loc=4) # bottom right
    plt.title("Various Normal cdfs")
    plt.show()
draw_binomial_dist()

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

#for i in range(16):
#    print 'xxx', i, compute_pvalue(15, 0.9, i)

def compute_num_from_pvalue(n, p, alpha=0.05):
    # find the max value that is < alpha
    # suppose m2 = 0, 1, 2 all < alpha, return 2
    # need to optimize this routine
    find_the_value = False
    m2 = 0
    saved_pvalue = 0.0

    for i in range(n+1):
        pvalue = compute_pvalue(n, p, i)
        #print 'yyy', i, pvalue
        if pvalue < alpha:
            find_the_value = True
            m2 = i
            saved_pvalue = pvalue
    if find_the_value == True:
        return m2, saved_pvalue
    return -1, 0

n=2
p=0.9
num, pvalue = compute_num_from_pvalue(n, p)
print 'if the number is <= ', num, "pvalue is ", pvalue, "we should reject"
print num/(n+0.0)
# if n=1000, p=0.9, the output is:
#if the number is <=  883 pvalue is  0.043343891238 we should reject
#0.883

# if I use the normal distribution, what's the output

# start with standard normal distribution



# normal distribution
def normal_dist(mu, se):

    return x

# from the book "data science from scratch"
def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))


def draw_pdf():
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs,[normal_pdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
    plt.plot(xs,[normal_pdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
    #plt.plot(xs,[normal_pdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
    #plt.plot(xs,[normal_pdf(x,mu=-1)   for x in xs],'-.',label='mu=-1,sigma=1')
    plt.legend()
    plt.title("Various Normal pdfs")
    plt.show()

def normal_cdf(x, mu=0,sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def draw_cdf():
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs,[normal_cdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
    plt.plot(xs,[normal_cdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
    #plt.plot(xs,[normal_cdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
    #plt.plot(xs,[normal_cdf(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')
    plt.legend(loc=4) # bottom right
    plt.title("Various Normal cdfs")
    plt.show()
#draw_pdf()
#draw_cdf()

def gaussian(x,sigma=1.0):
    exp=math.e**(-x**2/(2*sigma**2))
    return (1/(sigma*(2*math.pi)**.5))*exp


# from stackoverflow
#if you accidentally write scipy.stats.norm(mean=100, std=12) instead of scipy.stats.norm(100, 12) or scipy.stats.norm(loc=100, scale=12),
#then it'll accept it, but silently discard those extra keyword arguments and give you the default (0,1).
scipy.stats.norm(0, 1)
print scipy.stats.norm(0, 1).pdf(-1.96)
print scipy.stats.norm(0, 1).cdf(-1.96) #0.025
print scipy.stats.norm(0, 2).pdf(-3.92), 'zzzzzzzzzzzz' #0.025


print math.e, math.e**3
print math.exp(3)
mu = 2
se = 1
z = -1.96
x = z*se + mu
print scipy.stats.norm(mu, se).pdf(x), 'xyz'
print scipy.stats.norm(mu, se).cdf(x), 'xyz'


print normal_pdf(x, mu = mu, sigma = se), 'xxxxx'
print normal_cdf(x, mu = mu, sigma = se), 'xxxxx'


# plot
print 'xxxxxxx', gaussian(-1)
#print 'xxxxxxx', gaussian(0)
#print 'xxxxxxx', gaussian(1)
