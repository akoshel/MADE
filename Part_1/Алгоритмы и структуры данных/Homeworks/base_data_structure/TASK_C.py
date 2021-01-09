import sys

class Dynamic_array:
    def __init__(self):
        self.len = 0
        self.capacity = 2
        self.A = [0] * 2
        self.begin = -1
        self.start = 0

    def __getitem__(self, k):
        return self.A[k]

    def _resize(self, new_cap, remove_flag):
        B = [0] * new_cap
        if remove_flag:
            for k, element in enumerate(self.A[self.begin: self.len]):
                B[k] = element
        else:
            for k, element in enumerate(self.A[self.begin + 1: self.capacity] + self.A[self.start: self.begin + 1]):
                B[k] = element
        self.A = B
        self.capacity = new_cap
        self.begin = self.len - 1
        self.start = 0

    def insert_at(self, val):
        if self.len == self.capacity:
            self._resize(2 * self.capacity, False)
        if self.begin == self.capacity - 1:
            self.begin = 0
            index = 0
        else:
            self.begin += 1
            index = self.begin
        for i in range(self.len - 1, index - 1, -1):
            self.A[i + 1] = self.A[i]

        self.A[index] = val
        self.len += 1

    def remove_at(self):
        if 4 * self.len == self.capacity:
            self._resize(int(self.capacity / 2), True)
        if self.begin + 1 == self.len or self.len == 0:
            index = self.start
            self.begin = 0
        else:
            index = self.start
        remove_value = self.A[index]
        if index == self.len - 1:
            self.A[index] = 0
            self.len -= 1
            return remove_value
        self.A[self.start] = 0
        self.start += 1
        #for i in range(index, self.len - 1):
        #    self.A[i] = self.A[i + 1]
        self.len -= 1
        return remove_value


class Queue:
    def __init__(self):
        self.items = Dynamic_array()

    def add(self, value):
        self.items.insert_at(value)

    def remove(self):
        return self.items.remove_at()

queue = Queue()
queue.add(7)
queue.add(2)
print([queue.items.A[i] for i in range(queue.items.len)], queue.items.len, queue.items.begin, queue.items.capacity)
queue.add(3)
queue.add(6)
print([queue.items.A[i] for i in range(queue.items.len)], queue.items.len, queue.items.begin, queue.items.capacity)
queue.add(15)
print([queue.items.A[i] for i in range(queue.items.len)], queue.items.len, queue.items.begin, queue.items.capacity)
queue.remove()
print([queue.items.A[i] for i in range(queue.items.len)], queue.items.len, queue.items.begin, queue.items.capacity)
queue.remove()
print([queue.items.A[i] for i in range(queue.items.len)], queue.items.len, queue.items.begin, queue.items.capacity)
queue.remove()
print([queue.items.A[i] for i in range(queue.items.len)], queue.items.len, queue.items.begin, queue.items.capacity)
queue.remove()
print([queue.items.A[i] for i in range(queue.items.len)], queue.items.len, queue.items.begin, queue.items.capacity)

queue.add(7)
queue.add(2)
queue.add(3)
queue.add(6)
queue.add(15)
print([queue.items.A[i] for i in range(queue.items.len)], queue.items.len, queue.items.begin, queue.items.capacity)
queue.remove()
print([queue.items.A[i] for i in range(queue.items.len)], queue.items.len, queue.items.begin, queue.items.capacity)
queue.remove()
print([queue.items.A[i] for i in range(queue.items.len)], queue.items.len, queue.items.begin, queue.items.capacity)
queue.remove()
print([queue.items.A[i] for i in range(queue.items.len)], queue.items.len, queue.items.begin, queue.items.capacity)
queue.remove()
print([queue.items.A[i] for i in range(queue.items.len)], queue.items.len, queue.items.begin, queue.items.capacity)
queue.remove()
print([queue.items.A[i] for i in range(queue.items.len)], queue.items.len, queue.items.begin, queue.items.capacity)

'''
num_of_operations = int(sys.stdin.readline())
for i in range(num_of_operations):
    inp = sys.stdin.readline().split(' ')
    if inp[0] == '+':
        queue.add(int(inp[1]))
    else:
        print(queue.remove())'''