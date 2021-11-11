class WeightedQuickUnion:
    def __init__(self, n: int):
        self.n = n
        self.id = list(range(n))
        self.size = [1 for _ in range(n)]
        self.num_components = n

    def find(self, p: int) -> int:
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p: int, q: int) -> None:
        root_p, root_q = self.find(p), self.find(q)

        if root_p != root_q:
            if self.size[root_p] < self.size[root_q]:
                self.id[root_p] = root_q
                self.size[root_q] += self.size[root_p]
            else:
                self.id[root_q] = root_p
                self.size[root_p] += self.size[root_q]

            self.num_components -= 1

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def count(self) -> int:
        return self.num_components


if __name__ == '__main__':
    with open('input.txt', 'r') as fin:
        n = int(fin.readline())
        print(f'n={n}')

        uf = WeightedQuickUnion(n)

        for line in fin:
            nodes = [int(i) for i in line.strip().split()]
            p, q = nodes[0], nodes[1]

            print(f'connect ({p}, {q})')
            if uf.connected(p, q):
                print(f'p={p}, q={q} is already connected')
            else:
                uf.union(p, q)

        connected_components = uf.count()
        assert connected_components == 2, f'# of components = {connected_components}'
