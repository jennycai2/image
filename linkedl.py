#
class MaxSizeList(object):
    def __init__(self, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.maxLen = value
        self.strings = []

    def print_strings(self, str1):
        print str1

    def push(self, str1):
        self.print_strings(str1)
        if len(self.strings) < self.maxLen:
            self.strings.append(str1)
        else:
            self.strings.pop()
            self.strings.append(str1)
    def get_list(self):
        return self.strings

num1 = MaxSizeList(1)

num1.push('hi')
num1.push('hi again')
print num1.get_list()

num1.push('hi the third time')
print num1.get_list()
