class UF:
    # given n nodes
    def __init__(self, n: int):
        pass

    # connect p and q
    def union(self, p: int, q: int) -> None:
        pass

    # p and q are connected?
    def connected(self, p: int, q: int) -> bool:
        pass

    # return compnoent id of p
    def find(self, p: int) -> int:
        pass

    # return # of components
    def count(self) -> int:
        pass


if __name__ == '__main__':
    with open('input/uf.txt', 'r') as fin:
        n = int(fin.readline())
        print(f'n={n}')

        uf = UF(n)

        for line in fin:
            p, q = [int(i) for i in line.strip().split()]
            if uf.find(p) == uf.find(q):
                continue
            print(f'connect ({p}, {q})')
            uf.union(p, q)

        assert uf.count() == 2, f'# of components={uf.count()}'
