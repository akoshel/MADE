import sys

class Dynamic_array:
    def __init__(self):
        self.capacity = 2
        self.A = [0] * 2
        self.front = -1
        self.rear = -1

    def __getitem__(self, k):
        return self.A[k]

    def _resize(self, new_cap, remove_flag):
        B = [0] * new_cap
        if remove_flag:
            for k, element in enumerate(self.A[self.front: self.rear + 1]):
                B[k] = element
            self.A = B
            self.rear = self.rear - self.front
            self.front = 0
            self.capacity = new_cap
        else:
            for k, element in enumerate(self.A[self.front: self.capacity] + self.A[0: self.front]):
                B[k] = element
            self.A = B
            self.rear = self.capacity - 1
            self.front = 0
            self.capacity = new_cap



    def insert(self, value):

        if ((self.rear + 1) % self.capacity == self.front):
            self._resize(2 * self.capacity, False)

        if (self.front == -1):
            self.front = 0
            self.rear = 0
            self.A[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.A[self.rear] = value

    def remove(self):

        if 4 * (self.rear - self.front) == self.capacity:
            self._resize(int(self.capacity / 2), True)

        if (self.front == self.rear):
            temp = self.A[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.A[self.front]
            self.front = (self.front + 1) % self.capacity
            if self.capacity == self.rear and self.front + 1 == self.rear:
                self.front = -1
                self.rear = -1
            return temp


class Queue:
    def __init__(self):
        self.items = Dynamic_array()

    def add(self, value):
        self.items.insert(value)

    def remove(self):
        return self.items.remove()

queue = Queue()
num_of_operations = int(sys.stdin.readline())
for i in range(num_of_operations):
    inp = sys.stdin.readline()
    if inp[0] == '+':
        queue.add(int(inp.split(' ')[1]))
    elif inp[0] == '-':
        print(queue.remove())