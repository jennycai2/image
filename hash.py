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
        new_node = ListNode(val)
        key = self.hash_function(val)
        if self.list1[key] == None:
            self.list1[key] = new_node
        else:
            node = self.list1[key]
            while (node.next):
                node = node.next
            node.next = new_node
        return True

    def delete(self, val):
        # if it is the last one
        return True

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
            cnt += self.number_exists(num1, num2, list1[i+1:])
        return cnt

input1 = [1,2,3,4,9,3,2,1]
sum_range = [5,6] # find all pairs whose sum is in this range (inclusive)
sol1 = Solution1()
x = sol1.two_sum(input1, sum_range)
print x
