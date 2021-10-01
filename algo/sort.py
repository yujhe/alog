from typing import Tuple


def less(p, q) -> bool:
    return p < q


def exchange(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def is_sorted(a) -> bool:
    for i in range(1, len(a)):
        if less(a[i], a[i-1]):
            return False
    return True


class Selection:
    def __init__(self):
        pass

    def sort(self, a):
        for i in range(len(a)):
            min = i
            for j in range(i+1, len(a)):
                if less(a[j], a[min]):
                    min = j
            exchange(a, i, min)


class Insertion:
    def __init__(self):
        pass

    def sort(self, a):
        for i in range(len(a)):
            for j in range(i, 0, -1):
                if less(a[j], a[j-1]):
                    exchange(a, j, j-1)
                else:
                    break


class Shell:
    def __init__(self):
        pass

    def sort(self, a):
        h = 1
        while h < len(a)//3:
            h = 3*h+1

        while h >= 1:
            for i in range(h, len(a), 1):
                for j in range(i, 0, -h):
                    if less(a[j], a[j-h]):
                        exchange(a, j, j-h)
                    else:
                        break
            h = h//3


class Merge:
    def __init__(self):
        pass

    def merge(self, a, aux, lo: int, mid: int, hi: int) -> None:
        i, j = lo, mid + 1
        for k in range(lo, hi + 1):
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i += 1
            elif aux[i] < aux[j]:
                a[k] = aux[i]
                i += 1
            else:
                a[k] = aux[j]
                j += 1

    def _sort(self, a, aux, lo, hi) -> None:
        if lo >= hi:
            return

        mid = lo + (hi - lo) // 2
        self._sort(aux, a, lo, mid)
        self._sort(aux, a, mid + 1, hi)
        self.merge(a, aux, lo, mid, hi)

    # sort given list
    def sort(self, a) -> None:
        aux = a.copy()
        self._sort(a, aux, 0, len(a) - 1)


class MergeBU:
    def __init__(self):
        pass

    def merge(self, a, lo, mid, hi):
        aux = a.copy()

        i, j = lo, mid+1
        for k in range(lo, hi+1, 1):
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i += 1
            elif less(aux[i], aux[j]):
                a[k] = aux[i]
                i += 1
            else:
                a[k] = aux[j]
                j += 1

    def sort(self, a):
        i = 1
        while i < len(a):
            for j in range(0, len(a)-i, i*2):
                self.merge(a, j, j+i-1, min(j+2*i-1, len(a)-1))
            i *= 2


class Quick:
    def __init__(self):
        pass

    def partition(self, a, lo: int, hi: int) -> int:
        i, j, k = lo + 1, hi, lo

        while True:
            while a[i] < a[k]:
                if i == hi:
                    break
                i += 1
            while a[j] > a[k]:
                j -= 1

            if i >= j:
                break

            exchange(a, i, j)
            i += 1
            j -= 1

        exchange(a, k, j)

        return j

    def _sort(self, a, lo, hi) -> None:
        if lo >= hi:
            return

        k = self.partition(a, lo, hi)
        self._sort(a, lo, k - 1)
        self._sort(a, k + 1, hi)

    # sort given list
    def sort(self, a) -> None:
        import random

        random.shuffle(a)
        self._sort(a, 0, len(a) - 1)


class Quick3Way:
    def __init__(self):
        pass

    def partition(self, a, lo: int, hi: int) -> Tuple[int, int]:
        i, lt, gt = lo, lo, hi
        v = a[lo]

        while i <= gt:
            if a[i] < v:
                exchange(a, i, lt)
                i += 1
                lt += 1
            elif a[i] > v:
                exchange(a, i, gt)
                gt -= 1
            else:
                i += 1

        return lt, gt

    def _sort(self, a, lo, hi) -> None:
        if lo >= hi:
            return

        lt, gt = self.partition(a, lo, hi)
        self._sort(a, lo, lt - 1)
        self._sort(a, gt + 1, hi)

    # sort given list
    def sort(self, a) -> None:
        import random

        random.shuffle(a)
        self._sort(a, 0, len(a) - 1)


class QuickSelect:
    def __init__(self):
        pass

    def partition(self, a, lo, hi) -> int:
        i, j = lo+1, hi

        while True:
            while less(a[i], a[lo]):
                if i == hi:
                    break
                i += 1
            while less(a[lo], a[j]):
                j -= 1

            if i >= j:
                break

            exchange(a, i, j)
            i += 1
            j -= 1

        exchange(a, lo, j)

        return j

    def select(self, a, k):
        import random

        random.shuffle(a)

        lo, hi = 0, len(a)-1
        while lo < hi:
            j = self.partition(a, lo, hi)
            if k < j:
                hi = j-1
            elif k > j:
                lo = j+1
            else:
                return a[k]
        return a[k]


class Heap:
    def __init__(self):
        pass

    def sort(self, a):
        n = len(a)
        a.insert(0, None)  # start from index 1
        for k in range(n//2, 0, -1):
            self._sink(a, k, n)

        k = n
        while k > 1:
            exchange(a, 1, k)
            k -= 1
            self._sink(a, 1, k)

        a.remove(None)

    def _sink(self, a, k, n):
        while 2*k <= n:
            j = 2*k
            if j < n and less(a[j], a[j+1]):
                j += 1

            if not less(a[k], a[j]):
                break
            exchange(a, k, j)
            k = j


if __name__ == '__main__':
    with open('input/sort.txt', 'r') as fin:
        words = fin.read().strip().split()

    sel_words = words.copy()
    Selection().sort(sel_words)
    assert is_sorted(sel_words), f'selection sort is not correct'

    ins_words = words.copy()
    Insertion().sort(ins_words)
    assert is_sorted(ins_words), f'insertion sort is not correct'

    she_words = words.copy()
    Shell().sort(she_words)
    assert is_sorted(she_words), f'shell sort is not correct'

    m_words = words.copy()
    Merge().sort(m_words)
    assert is_sorted(m_words), f'merge sort is not correct'

    m_bu_words = words.copy()
    MergeBU().sort(m_bu_words)
    assert is_sorted(m_bu_words), f'buttom-up merge sort is not correct'

    q_words = words.copy()
    Quick().sort(q_words)
    assert is_sorted(q_words), f'quick sort is not correct'

    q3_words = words.copy()
    Quick3Way().sort(q3_words)
    assert is_sorted(q3_words), f'3-way quick sort is not correct'

    h_words = words.copy()
    Heap().sort(h_words)
    assert is_sorted(h_words), f'heap sort is not correct: {h_words}'

    q_sel_words = words.copy()
    assert QuickSelect().select(q_sel_words, 0) == 'A', f'quick select is not correct'
    assert QuickSelect().select(q_sel_words, len(q_sel_words) - 1) == 'X', f'quick select is not correct'
