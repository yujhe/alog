def less(p, q):
    return p < q


def exchange(arr, p, q):
    temp = arr[p]
    arr[p] = arr[q]
    arr[q] = temp


class MinPQ:
    def __init__(self, n):
        self.key = [None] * (n+1)
        self.n = 0

    def insert(self, p):
        self.n += 1
        self.key[self.n] = p
        self._swim(self.n)

    def del_min(self):
        min = self.key[1]
        exchange(self.key, 1, self.n)
        self.key[self.n] = None
        self.n -= 1
        self._sink(1)

        return min

    def is_empty(self):
        return self.n == 0

    def min(self):
        return self.key[1]

    def size(self):
        return self.n

    def _swim(self, k):
        while k > 1 and less(self.key[k], self.key[k//2]):
            exchange(self.key, k, k//2)
            k = k//2

    def _sink(self, k):
        while 2*k <= self.n:
            j = 2*k
            if j < self.n and less(self.key[j+1], self.key[j]):
                j += 1
            if less(self.key[k], self.key[j]):
                break
            exchange(self.key, k, j)
            k = j


class MaxPQ:
    def __init__(self, n):
        self.key = [None] * (n+1)
        self.n = 0

    def insert(self, p):
        self.n += 1
        self.key[self.n] = p
        self._swim(self.n)

    def del_max(self):
        max = self.key[1]
        exchange(self.key, 1, self.n)
        self.key[self.n] = None
        self.n -= 1
        self._sink(1)

        return max

    def is_empty(self):
        return self.n == 0

    def max(self):
        return self.key[1]

    def size(self):
        return self.n

    def _swim(self, k):
        while k > 1 and less(self.key[k//2], self.key[k]):
            exchange(self.key, k, k//2)
            k = k//2

    def _sink(self, k):
        while 2*k <= self.n:
            j = 2*k
            if j < self.n and less(self.key[j], self.key[j+1]):
                j += 1
            if not less(self.key[k], self.key[j]):
                break
            exchange(self.key, k, j)
            k = j


if __name__ == '__main__':
    ops = [
        2, 8, 1, '-', 9, 8, 4, 4, 4, '-', '-', '-', '-'
    ]
    min_out = [1, 2, 4, 4, 4]
    max_out = [8, 9, 8, 4, 4]

    min_pq = MinPQ(10)
    min_pq_out = []

    max_pq = MaxPQ(10)
    max_pq_out = []

    for op in ops:
        if op == '-':
            min_pq_out.append(min_pq.del_min())
            max_pq_out.append(max_pq.del_max())
        else:
            min_pq.insert(op)
            max_pq.insert(op)

    assert min_pq_out == min_out and min_pq.size() == 3 and not min_pq.is_empty(
    ) and min_pq.min() == 8, f'min pq operations incorrect: queue={min_pq.key}, size={min_pq.size()}, empty={min_pq.is_empty()}, out={min_pq_out}'
    assert max_pq_out == max_out and max_pq.size() == 3 and not max_pq.is_empty(
    ) and max_pq.max() == 4, f'max pq operations incorrect: queue={max_pq.key}, size={max_pq.size()}, empty={max_pq.is_empty()}, out={max_pq_out}'
