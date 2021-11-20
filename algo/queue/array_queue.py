from typing import Iterator


class ArrayQueue:
    def __init__(self):
        self.arr = [None]
        self.n = 0
        self.head = 0
        self.tail = 0

    def enqueue(self, n: str) -> None:
        self.check()

        self.arr[self.tail] = n
        self.tail += 1
        self.tail %= len(self.arr)
        self.n += 1

    def dequeue(self) -> str:
        if self.is_empty():
            raise Exception('queue is empty')

        n = self.arr[self.head]
        self.arr[self.head] = None
        self.head += 1
        self.head %= len(self.arr)
        self.n -= 1

        self.check()

        return n

    def size(self) -> int:
        return self.n

    def is_empty(self) -> bool:
        return self.n == 0

    def iterator(self) -> Iterator[str]:
        return iter(self.arr[self.head:self.head+self.n])

    def check(self) -> None:
        arr_size = len(self.arr)

        if self.n == arr_size:
            self.resize(2 * arr_size)
        elif 0 < self.n <= arr_size / 4:
            self.resize(int(arr_size / 2))

    def resize(self, n: int) -> None:
        tmp = [None] * n

        for i in range(self.n):
            tmp[i] = self.arr[(self.head + i) % len(self.arr)]

        self.head = 0
        self.tail = self.n
        self.arr = tmp


if __name__ == '__main__':
    queue = ArrayQueue()
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
