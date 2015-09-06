#
"""
Your task is to compute the number of target values t in the interval [-10000,10000] (inclusive)
such that there are distinct numbers x,y in the input file that satisfy x+y=t.
 (NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)
"""

class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class hashTable(object):
    def __init__(self, n):
        self.size = n
        self.list1 = [None]*n

    def hash_function(self, val):
        return val % self.size

    def insert(self, val):
        key = self.hash_function(val)
        if self.list1[key] == None:
            self.list1[key] = ListNode(val)
        else:
            node = self.list1[key]
            while (node.next):
                if node.val == val:
                    return True  # we don't insert duplicate value
                node = node.next
            node.next = ListNode(val) # no value is same as it, insert it
        return True

    def delete(self, val):
        # if it is the last one
        key = self.hash_function(val)
        if self.list1[key] == None:
            return False

        node = self.list1[key]
        if node.val == val:
            if node.next:
                # need to remove the head node
                self.list1[key] = node.next
            else:
                # it's the only node
                self.list1[key] = None
            return True
        while (node.next):
            if (node.next.val == val):
                node.next = node.next.next
                return True
            node = node.next

        return False

    def lookup(self, val):
        key = self.hash_function(val)
        node = self.list1[key]
        if node == None:
            return False
        while node.next:
            if node.val == val:
                return True
            node = node.next
        return False

    def lookup_range(self, num1, num2):
        cnt = 0
        for i in range(num1, num2+1):
            if self.lookup(i):
                cnt += 1
        return cnt

class Solution1(object):
    def number_exists(self, num1, num2, list2):
        print 'list2 ', list2
        cnt = 0
        for i in range(len(list2)):
            if list2[i] <= num2 and list2[i] >= num1:
                print 'indx ', i
                cnt += 1
        return cnt

    def two_sum(self, list1, sum_range):
        htable = hashTable(3)
        for i in range(len(list1)):
            htable.insert(list1[i])

        cnt = 0
        for i in range(len(list1)):
            num1 = sum_range[0] - list1[i]
            num2 = sum_range[1] - list1[i]
            cnt += htable.lookup_range(num1, num2)
            if list1[i] <= num2 and list1[i] >= num1:
                cnt -= 1  # we should count self twice
        return cnt/2  # since each pair is counted twice

input1 = [1,2,3,4,9,3,2,1]
sum_range = [5,6] # find all pairs whose sum is in this range (inclusive)
sol1 = Solution1()
x = sol1.two_sum(input1, sum_range)
print x
