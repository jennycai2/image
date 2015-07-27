import math

def num_occurance(number1, numbers):
    cnt = 0
    for i in range(len(numbers)):
        if number1 == numbers[i]:
           cnt +=1
    return cnt

def compute_entropy(numbers):
    n = len(numbers)
    if (n<=0):
        return -1.0 # it's an error situation
    p = 1/float(n)
    set1 = set(numbers)
    number1 = list(set1)
    n1 = len(set1)
    total = 0.0
    for i in range(n1):
        p = num_occurance(number1[i], numbers)/ float(n)
        print 'xxxxxx, p', p
        total -= (p * math.log(p))

    return total

x = [1]
entr = compute_entropy(x)
print  'xxxx, entropy', entr

x = [3, 3, 3]
entr = compute_entropy(x)
print  'xxxx, entropy', entr
x = [1, 3, 3]
entr = compute_entropy(x)
print  'xxxx, entropy', entr
x = [1, 2, 3]
entr = compute_entropy(x)
print  'xxxx, entropy', entr
