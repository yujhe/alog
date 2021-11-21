from typing import Iterator


class LinkedQueue:
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def enqueue(self, n: str) -> None:
        node = self.Node(n)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.n += 1

    def dequeue(self) -> str:
        if self.is_empty():
            raise Exception('queue is empty')

        n = self.head
        self.head = n.next
        self.n -= 1

        if self.size() == 0:
            self.tail = None

        return n.item

    def size(self) -> int:
        return self.n

    def is_empty(self) -> bool:
        return self.n == 0

    def __iter__(self):
        self.x = self.head
        return self

    def __next__(self):
        if self.x:
            n = self.x.item
            self.x = self.x.next
            return n
        else:
            raise StopIteration

    def iterator(self) -> Iterator[str]:
        return iter(self)


if __name__ == '__main__':
    queue = LinkedQueue()
    out = []

    with open('input.txt', 'r') as fin:
        for line in fin:
            for op in line.split():
                if op == '-':
                    out.append(queue.dequeue())
                else:
                    queue.enqueue(op)

    assert out == ['to', 'be', 'or', 'not', 'to', 'be'], f'out={out}'
    assert queue.size() == 2, f'size={queue.size()}'
    assert list(queue.iterator()) == ['that', 'is'], f'queue={list(queue.iterator())}'
