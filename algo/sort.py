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
        pass

    def _sort(self, a, aux, lo, hi) -> None:
        pass

    # sort given list
    def sort(self, a) -> None:
        pass


class MergeBU:
    def __init__(self):
        pass

    def merge(self, a, lo, mid, hi):
        pass

    def sort(self, a):
        pass


class Quick:
    def __init__(self):
        pass

    def partition(self, a, lo: int, hi: int) -> int:
        pass

    def _sort(self, a, lo, hi) -> None:
        pass

    # sort given list
    def sort(self, a) -> None:
        pass


class Quick3Way:
    def __init__(self):
        pass

    def partition(self, a, lo: int, hi: int) -> Tuple[int, int]:
        pass

    def _sort(self, a, lo, hi) -> None:
        pass

    # sort given list
    def sort(self, a) -> None:
        pass


class QuickSelect:
    def __init__(self):
        pass

    def partition(self, a, lo, hi) -> int:
        pass

    def select(self, a, k):
        pass


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
