import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        node = self.head
        nodes = []
        while node != None:
            nodes.append(node.value)
            node = node.next
        nodes.append(None)
        return ('->'.join(list(map(str, nodes))))

    def add_first(self, node):
        node.next = self.head
        self.head = node
        self.size += 1

    def add_last(self, node):
        self.tail.next = node
        self.tail = node
        self.size += 1

    def add_after(self, target_value, new_node):
        node = self.head
        while node is not None:
            if node.value == target_value:
                new_node.next = node.next
                node.next = new_node
                self.size += 1
                break
            else:
                node = node.next

    def remove_node(self, target_value):
        if self.head.value == target_value:
            self.head = self.head.next
            return
        previous_node = self.head
        node = self.head
        while node != None:
            node = node.next
            if node.value == target_value:
                if previous_node.next == self.tail:
                    self.tail = previous_node
                previous_node.next = node.next
                self.size -= 1
                return
            previous_node = node


class Stack:

    def __init__(self):
        self.stack = LinkedList()
        self.min = None

    def push(self, value):
        if self.stack.head == None:
            self.stack.head = Node(value)
            self.min = value
        else:
            self.stack.add_first(Node(value))
            if self.min > value:
                self.min = value

    def pop(self):
        remove_value = self.stack.head.value
        self.stack.remove_node(remove_value)
        if remove_value == self.min:
            self.find_min()
        return remove_value
# напиши find_min
    def find_min(self):
        if self.stack.head == None:
            self.min = None
            return
        node = self.stack.head
        self.min = node.value
        while node.next != None:
            node = node.next
            if node.value < self.min:
                self.min = node.value
                return
        return

    def show_min(self):
        sys.stdout.write(str(self.min) + '\n')

stack = Stack()

n = int(sys.stdin.readline())
for i in range(n):
    inp_list = list(map(int, sys.stdin.readline().split(' ')))
    if inp_list[0] == 1:
        stack.push(inp_list[1])
    elif inp_list[0] == 2:
        stack.pop()
    else:
        stack.show_min()