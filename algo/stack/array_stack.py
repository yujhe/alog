from typing import Iterator


class ArrayStack:
    def __init__(self):
        self.arr = [None]
        self.n = 0

    def push(self, n: str) -> None:
        self.check()
        self.arr[self.n] = n
        self.n += 1

    def pop(self) -> str:
        if self.is_empty():
            raise Exception('stack is empty')

        v = self.arr[self.n-1]
        self.n -= 1
        self.arr[self.n] = None
        self.check()

        return v

    def is_empty(self) -> bool:
        return self.n == 0

    def size(self) -> int:
        return self.n

    def iterator(self) -> Iterator[str]:
        return iter(self.arr)

    def check(self) -> None:
        arr_size = len(self.arr)

        if self.n == arr_size:
            self.resize(2 * arr_size)
        elif 0 < self.n <= int(arr_size / 4):
            self.resize(int(arr_size / 2))

    def resize(self, new_size: int) -> None:
        new_arr = [None] * new_size

        for i in range(self.n):
            new_arr[i] = self.arr[i]

        self.arr = new_arr


if __name__ == '__main__':
    stack = ArrayStack()
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
    assert list(stack.iterator()) == ['to', 'is'], f'stack={list(stack.iterator())}'
