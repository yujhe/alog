class UF:
    # given n nodes
    def __init__(self, n: int):
        self.n = n
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_component = n

    # connect p and q
    def union(self, p: int, q: int) -> None:
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p == root_q:
            return

        if self.size[root_p] < self.size[root_q]:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        else:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]

        self.num_component -= 1

    # p and q are connected?
    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    # return compnoent id of p
    def find(self, p: int) -> int:
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]

        return p

    # return # of components
    def count(self) -> int:
        return self.num_component


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
