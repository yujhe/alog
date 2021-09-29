class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedStack:
    def __init__(self):
        self.first = None
        self.count = 0

    def push(self, item):
        temp = self.first
        self.first = Node(item)
        self.first.next = temp
        self.count += 1

    def pop(self):
        n = self.first
        self.first = self.first.next
        self.count -= 1

        return n.item

    def is_empty(self):
        return self.first == None

    def size(self):
        return self.count


class ArrayStack:
    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def pop(self):
        return self.s.pop()

    def is_empty(self):
        return self.s == []

    def size(self):
        return len(self.s)


class LinkedQueue:
    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0

    def enqueue(self, item):
        oldlast = self.last
        self.last = Node(item)
        if self.is_empty():
            self.first = self.last
        else:
            oldlast.next = self.last
        self.count += 1

    def dequeue(self):
        n = self.first
        self.first = self.first.next
        if self.is_empty():
            self.last = None
        self.count -= 1

        return n.item

    def is_empty(self):
        return self.first == None

    def size(self):
        return self.count


class ArrayQueue:
    def __init__(self):
        self.q = []

    def enqueue(self, item):
        self.q.insert(0, item)

    def dequeue(self):
        return self.q.pop()

    def is_empty(self):
        return self.q == []

    def size(self):
        return len(self.q)


if __name__ == '__main__':
    ops = [
        'to', 'be', 'or', 'not', 'to', '-', 'be', '-', '-', 'that', '-', '-', '-', 'is'
    ]
    s_out = ['to', 'be', 'not', 'that', 'or', 'be']
    q_out = ['to', 'be', 'or', 'not', 'to', 'be']

    a_stack = ArrayStack()
    a_stack_out = []

    l_stack = LinkedStack()
    l_stack_out = []

    a_queue = ArrayQueue()
    a_queue_out = []

    l_queue = LinkedQueue()
    l_queue_out = []

    for op in ops:
        if op == '-':
            a_stack_out.append(a_stack.pop())
            l_stack_out.append(l_stack.pop())
            a_queue_out.append(a_queue.dequeue())
            l_queue_out.append(l_queue.dequeue())
        else:
            a_stack.push(op)
            l_stack.push(op)
            a_queue.enqueue(op)
            l_queue.enqueue(op)

    assert (a_stack_out == s_out and a_stack.size() ==
            2 and not a_stack.is_empty()), 'array stack check failed'
    assert (l_stack_out == s_out and l_stack.size() ==
            2 and not l_stack.is_empty()), 'linked stack check failed'
    assert(a_queue_out == q_out and a_queue.size() ==
           2 and not a_queue.is_empty()), 'array queue check failed'
    assert(l_queue_out == q_out and l_queue.size() ==
           2 and not l_queue.is_empty()), 'linked queue check failed'
