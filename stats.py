# statistics

import math

from matplotlib import pyplot as plt
import scipy.stats
# a medicine cures 90% of patients. Is it true?
# or a loaded coin with p(Heads) = 0.9
# treat n patients
# flip the coin n times
# (n+1) outcomes, with the heads showing up 0, 1, 2,..., or n times



def compute_mean_var(sample):
    total = 0.0
    n = len(sample)
    for i in range (n):
        total += sample[i]
    mean1 = total/n
    total = 0.0
    for i in range(n):
        total += (sample[i] - mean1)**2
    var1 = total/(n-1)
    sd = math.sqrt(var1)
    se = sd/math.sqrt(n)
    intervals = (mean1-1.96*se, mean1+1.96*se)

    return mean1, var1, sd, se, intervals


class Solution1(object):
    def factorial(self, n):
        if n<=1:
            return 1
        return n* self.factorial(n-1)

    def compute_chi_square(self):
        input0 = [1,2,3,4]
        a = input0[0]
        b = input0[1]
        c = input0[2]
        d = input0[3]
        pobserved = (a+d)/(a+b+c+d)
        pexpected = ((a + c)*(a + b))/(a + b + c + d)**2 + ((b + d)*(c + d))/(a + b + c + d)**2
        K = (pobserved - pexpected)/(1.0-pexpected)
        return pobserved, pexpected, K

    def compute_kappa(self):
        a = 70.0
        b = 15.0
        c = 30.0
        d = 25.0
        pobserved = (a+d)/(a+b+c+d)
        pexpected = ((a + c)*(a + b))/(a + b + c + d)**2 + ((b + d)*(c + d))/(a + b + c + d)**2
        K = (pobserved - pexpected)/(1.0-pexpected)
        return pobserved, pexpected, K

    def compute_correlation_r_t_rsquare(self, list1, list2):
        if len(list1) == 0:
            return -2
        if len(list1) != len(list2):
            return -2
        mean1, var1, sd, se, intervals = compute_mean_var(list1)
        mean2, var2, sd, se, intervals = compute_mean_var(list2)
        sum12 = 0.0
        sum11 = 0.0
        sum22 = 0.0
        for i in range(len(list1)):
            sum12 += (list1[i] - mean1)* (list2[i] - mean2)
            sum11 += (list1[i] - mean1)* (list1[i] - mean1)
            sum22 += (list2[i] - mean2)* (list2[i] - mean2)
        r = sum12 / math.sqrt(sum11*sum22)
        n = len(list1)
        t = r * math.sqrt(n-2)/math.sqrt(1-r**2)
        return r, t, r**2

list0 = [61, 64, 68, 70, 70, 71, 73, 74, 74, 76, 79, 80, 80, 83, 84, 84, 87, 89, 89, 89, 90, 92, 95, 95, 98, 100]
list1 = [60,62,63,65,65,67,68,70,70,71]
list2 = [103,100,98,95,110,108,104,110,97,100]

list1 = [1,2,3,4,5,6,7,8,9,10]
list1 = [29,31,35,39,39,40,43,44,44,52]

def compute_percentile(lst, k):

    lst.sort()
    #print lst
    n = len(lst)
    x = k*(n+1)/100.0
    idx = int(x)
    r = x - idx
    val = lst[idx-1]*(1-r) + lst[idx]*r
    return n, x, idx, lst[idx],val

print compute_percentile(list1, 25)
print compute_percentile(list1, 50)
print compute_percentile(list1, 75)



sol1 = Solution1()
r, t, rs = sol1.compute_correlation_r_t_rsquare(list1, list2)
#print r, t, rs
#print 'kappa ', sol1.compute_kappa()

#for i in range(10):
#    print i, 'factorial ', sol1.factorial(i)

def compute_t(xbar, mu, s, n):
    t = (xbar - mu)/s * math.sqrt(n)
    return t
#print compute_t(3.867, 5, 1.995, 15)

def compute_permutation(n, x):
    res = 1
    for i in range (x):
        res *= (n-i)
    #print res
    return res


#Write code to take an input string say 'abc' and parameter value as 2... code
#output should be ALL combinations of 2 letter words possible from the string input such as ab, ac, bc, ba, ca, cb etc

def substring(string1, k):
    n = len(string1)
    if (n<=k):
        return string1
    c=[]
    for i in range(n):
        c.append(string1[i])
    output = []
    for i in range(n):
        for j in range(n):
            if i!=j:
                output.append(c[i] + c[j])
    return output

#print substring('abc', 2)

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

#print 'zzz', compute_combination(14,9), 0.0062/math.sqrt(1/5000.0+1/5000.0)*math.sqrt(1/27948.0 + 1/28052.0)

# comput binomial distribution probability
def compute_prob(n, p, x):
    return p**x * (1-p)**(n-x) * compute_combination(n, x)
sum2 = 0.0
for i in range (9, 15):
    sum2+=compute_prob(14, 0.5, i)
#print 'sum2', sum2



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
#draw_binomial_dist()

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
#print compute_combined_prob(100, 0.9, 0, 80), 'xxx1111111111'

def compute_pvalue(n, p, m):
    return compute_combined_prob(n,p,0,m)
#print compute_pvalue(14, 0.5, 9), '11111111111'
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
#print 'if the number is <= ', num, "pvalue is ", pvalue, "we should reject"
#print num/(n+0.0)
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
#print scipy.stats.norm(0, 1).pdf(-1.96)
#print scipy.stats.norm(0, 1).cdf(-1.96) #0.025
#print scipy.stats.norm(0, 2).pdf(-3.92), 'zzzzzzzzzzzz' #0.025

#from scipy.stats import norm
#norm.cdf(1.96)

# the inverse CDF:
# This is like to look up the Z table
# the first value is mean, the second value is standard deviation
# cdf, cumulative, probablity for minus infini to this value
# ppf, from probablity to value
"""
print scipy.stats.norm(0, 1).ppf(0.05), 'pppppppppp'
print scipy.stats.norm(0, 1).ppf(0.025), 'pppppppppp' # 95% confidence interval
print scipy.stats.norm(0, 1).ppf(0.1), 'pppppppppp' # 80% confidence internal
print scipy.stats.norm(0, 1).ppf(0.2), 'pppppppppp' # 80% CI, one-tailed
print scipy.stats.norm(0, 1).cdf(-1.46)*2 , 'CDF' # two-tailed, *2
print scipy.stats.norm(0, 1).cdf(-0.66)*2 , 'CDF'
print scipy.stats.norm(0, 1).cdf(-1.41)*2, 'CDF'
print scipy.stats.norm(0, 1).cdf(-1.79), 'CDF'
print scipy.stats.t.cdf(-2.17, 14), 'T'
print scipy.stats.t.ppf(-2.17, 14), 'T'
print scipy.stats.t.ppf(1-0.05, 14)

print scipy.stats.norm(100, 15).cdf(80), 'CDF'
print scipy.stats.norm(100, 2).cdf(95), 'CDF'
print scipy.stats.norm(100, 2).cdf(98), 'CDF'
"""
xbar = 3.867
p = 1.761
n = 15
x = xbar + (p * 1.995 / math.sqrt(n))
#rint 'x = ', x
#print scipy.stats.norm(0, 1).ppf(0.05), 'pppppppppp'
#print (1.0 - scipy.stats.norm(80, 4).cdf(85.1)), 'pppppppppp'

x = 10*9/2*(0.2)**2*0.8**8
x2 = 10*(0.2)**1*0.8**9
#print 1-(x+x2+0.8**10)

#print math.e, math.e**3
#print math.exp(3)
mu = 2
se = 1
z = -1.96
x = z*se + mu
#print scipy.stats.norm(mu, se).pdf(x), 'xyz'
#print scipy.stats.norm(mu, se).cdf(x), 'xyz'
#print normal_pdf(x, mu = mu, sigma = se), 'xxxxx'
#print normal_cdf(x, mu = mu, sigma = se), 'xxxxx'


# plot
#print 'xxxxxxx', gaussian(-1)
#print 'xxxxxxx', gaussian(0)
#print 'xxxxxxx', gaussian(1)
