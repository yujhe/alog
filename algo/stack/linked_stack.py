class LinkedStack:
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self):
        self.head = None
        self.n = 0

    def push(self, n: str) -> None:
        node = self.Node(n)
        node.next = self.head

        self.head = node
        self.n += 1

    def pop(self) -> str:
        if self.is_empty():
            raise Exception('stack is empty')

        node = self.head
        self.head = node.next
        self.n -= 1

        return node.item

    def is_empty(self) -> bool:
        return self.n == 0

    def size(self) -> int:
        return self.n


if __name__ == '__main__':
    stack = LinkedStack()
    out = []

    with open('input.txt', 'r') as fin:
        for line in fin:
            for op in line.split():
                if op == '-':
                    out.append(stack.pop())
                else:
                    stack.push(op)

    assert out == ['to', 'be', 'not', 'that', 'or', 'be'], f'out={out}'
    assert stack.size() == 2, f'size={stack.size()}'
