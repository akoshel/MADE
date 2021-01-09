import sys

class Dynamic_array:
    def __init__(self):
        self.len = 0
        self.capacity = 1
        self.A = [0] * 2

    def __getitem__(self, k):
        return self.A[k]

    def _resize(self, new_cap):
        B = [0] * new_cap
        for k in range(self.len):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_cap

    def append(self, val):
        if self.len == self.capacity:
            self._resize(2 * self.capacity)
        self.A[self.len] = val
        self.len += 1

    def insert_at(self, val, index):
        if self.len == self.capacity:
            self._resize(2 * self.capacity)

        for i in range(self.len - 1, index - 1, -1):
            self.A[i + 1] = self.A[i]

        self.A[index] = val
        self.len += 1

    def remove_at(self, index):
        if 4 * self.len == self.capacity:
            self._resize(int(self.capacity / 2))
        if index == self.len - 1:
            self.A[index] = 0
            self.len -= 1
            return
        for i in range(index, self.len - 1):
            self.A[i] = self.A[i + 1]

        self.A[self.len - 1] = 0
        self.len -= 1


class Stack:

    def __init__(self):
        self.stack = Dynamic_array()

    def push(self, value):
        self.stack.insert_at(value, 0)

    def pop(self):
        remove_value = self.stack.A[0]
        self.stack.remove_at(0)
        return remove_value

    def operation(self, sign):
        if self.stack.len == 1:
            return
        a = self.pop()
        b = self.pop()
        if sign[0] == '+':
            self.push(b + a)
        elif sign[0] == '-':
            self.push(b - a)
        else:
            self.push(b * a)


stack = Stack()
input_list = sys.stdin.readline().split(' ')

for element in input_list:
    try:
        stack.push(int(element))
    except ValueError:
        stack.operation(element)

sys.stdout.write(str(stack.stack.A[0]) + '\n')
