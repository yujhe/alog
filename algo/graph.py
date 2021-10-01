from typing import Deque


class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [Deque() for _ in range(v)]

    # return # of vertices
    def V(self) -> int:
        return self.v

    # return # of edges
    def E(self) -> int:
        return int(sum([len(i) for i in self.adj]) / 2)

    # add edge between v and w
    def add_edge(self, v: int, w: int) -> None:
        self.adj[v].appendleft(w)
        self.adj[w].appendleft(v)

    # return the vertices adjacent to vertex v
    def get_adj(self, v: int) -> list[int]:
        return self.adj[v]

    # return the degree of vertex v
    def get_degree(self, v: int) -> int:
        return len(self.adj[v])


class Digraph:
    def __init__(self, v):
        self.v = v
        self.adj = [Deque() for _ in range(v)]
        self.indegree = [0] * v

    # return # of vertices
    def V(self) -> int:
        return self.v

    # return # of edges
    def E(self) -> int:
        return sum([len(i) for i in self.adj])

    # add edge between v and w
    def add_edge(self, v: int, w: int) -> None:
        self.adj[v].appendleft(w)
        self.indegree[w] += 1

    # return the vertices adjacent to vertex v
    def get_adj(self, v: int) -> list[int]:
        return self.adj[v]

    # return the indegree of vertex v
    def get_indegree(self, v: int) -> int:
        return self.indegree[v]

    # return the outdegree of vertex v
    def get_outdegree(self, v: int) -> int:
        return len(self.adj[v])

    # return the reverse of the digraph
    def reverse(self):
        g = Digraph(self.v)
        for v in range(self.v):
            for w in self.adj[v]:
                g.add_edge(w, v)

        return g


class DepthFirstPaths:
    def __init__(self, g: Graph, s: int):
        self.source = s
        self.visited = [False] * g.V()
        self.edge_to = [None] * g.V()

        self.dfs(g, s)

    # depth first search from v
    def dfs(self, g: Graph, v: int) -> None:
        self.visited[v] = True

        for w in g.get_adj(v):
            if not self.visited[w]:
                self.edge_to[w] = v
                self.dfs(g, w)

    # is there a path between source to v?
    def has_path_to(self, v: int) -> bool:
        return self.visited[v]

    # return a path between source to v
    def get_path_to(self, v: int) -> list[int]:
        if not self.has_path_to(v):
            return None

        path = Deque()
        while v != self.source:
            path.appendleft(v)
            v = self.edge_to[v]
        path.appendleft(self.source)

        return list(path)


class BreadthFirstPaths:
    def __init__(self, g: Graph, ss: list[int]):
        self.sources = ss
        self.visited = [False] * g.V()
        self.edge_to = [None] * g.V()
        self.dist_to = [None] * g.V()

        self.bfs(g, ss)

    # breadth first search from multiple sources
    def bfs(self, g: Graph, ss: list[int]) -> None:
        queue = Deque()
        for s in ss:
            self.visited[s] = True
            self.dist_to[s] = 0
            queue.append(s)

        while queue:
            v = queue.popleft()

            for w in g.get_adj(v):
                if not self.visited[w]:
                    self.visited[w] = True
                    self.edge_to[w] = v
                    self.dist_to[w] = self.dist_to[v] + 1
                    queue.append(w)

    # is there a path between source to v
    def has_path_to(self, v: int) -> bool:
        return self.visited[v]

    # return the # of edges in a shortest path between source and v
    def get_dist_to(self, v: int) -> int:
        return self.dist_to[v]

    # return the shortest path between source and v
    def get_path_to(self, v: int) -> list[int]:
        if not self.has_path_to(v):
            return None

        path = Deque()
        while v not in self.sources:
            path.appendleft(v)
            v = self.edge_to[v]
        path.appendleft(v)

        return list(path)


class DepthFirstOrder:
    def __init__(self, g: Digraph):
        self.visited = [False] * g.V()
        self.pre = [0] * g.V()
        self.post = [0] * g.V()
        self.preorder = []
        self.postorder = []

        self.precounter = 0
        self.postcounter = 0

        for i in range(g.V()):
            if not self.visited[i]:
                self.dfs(g, i)

    # depth first search for a graph
    def dfs(self, g: Graph, v: int) -> None:
        self.visited[v] = True

        self.pre[v] = self.precounter
        self.precounter += 1
        self.preorder.append(v)
        for w in g.get_adj(v):
            if not self.visited[w]:
                self.dfs(g, w)
        self.post[v] = self.postcounter
        self.postcounter += 1
        self.postorder.append(v)

    # return the preorder number of v
    def get_preorder(self, v: int) -> int:
        return self.pre[v]

    # return the postorder number of v
    def get_postorder(self, v: int) -> int:
        return self.post[v]

    # return the vertices in preorder
    def get_pre(self) -> list[int]:
        return self.preorder

    # return the vertices in postorder
    def get_post(self) -> list[int]:
        return self.postorder

    # return the vertices in reverse postorder
    def get_reverse_post(self) -> list[int]:
        return list(reversed(self.postorder))


class ConnectedComponent:
    def __init__(self, g: Graph):
        self.visited = [False] * g.V()
        self.cid = [None] * g.V()
        self.size = {}
        self.count = 0

        for i in range(g.V()):
            if not self.visited[i]:
                self.dfs(g, i)
                self.count += 1

    # depth first search for a graph
    def dfs(self, g: Graph, v: int) -> None:
        self.visited[v] = True
        self.cid[v] = self.count
        self.size[self.count] = self.size.get(self.count, 0) + 1

        for w in g.get_adj(v):
            if not self.visited[w]:
                self.dfs(g, w)

    # return true if v and w are in the same connected component
    def connected(self, v: int, w: int) -> bool:
        return self.get_id(v) == self.get_id(w)

    # return # of connected components
    def get_count(self) -> int:
        return self.count

    # return # of vertices in the connected component containing v
    def get_size(self, v) -> int:
        return self.size[self.cid[v]]

    # return the component id of v
    def get_id(self, v: int) -> int:
        return self.cid[v]


class StrongConnectedComponents:
    def __init__(self, g: Digraph):
        self.visited = [False] * g.V()
        self.cid = [None] * g.V()
        self.csize = {}
        self.count = 0

        reversed_g = g.reverse()
        dfs_order = DepthFirstOrder(reversed_g)

        for v in dfs_order.get_reverse_post():
            if not self.visited[v]:
                self.dfs(g, v)
                self.count += 1

    # depth first seach for a graph
    def dfs(self, g: Digraph, v: int) -> None:
        self.visited[v] = True
        self.cid[v] = self.count
        self.csize[self.count] = self.csize.get(self.count, 0) + 1

        for w in g.get_adj(v):
            if not self.visited[w]:
                self.dfs(g, w)

    # return true if v and w are in the same connected component
    def connected(self, v: int, w: int) -> bool:
        return self.get_id(v) == self.get_id(w)

    # return # of connected components
    def get_count(self) -> int:
        return self.count

    # return # of vertices in the connected component containing v
    def get_size(self, v) -> int:
        return self.csize[self.get_id(v)]

    # return the component id of v
    def get_id(self, v: int) -> int:
        return self.cid[v]


class Cycle:
    def __init__(self, g: Graph):
        self.visited = [False] * g.V()
        self.edge_to = [None] * g.V()
        self.cycle = []

        for v in range(g.V()):
            if not self.visited[v]:
                self.dfs(g, -1, v)

    # depth first search from u to v
    def dfs(self, g: Graph, u: int, v: int) -> None:
        self.visited[v] = True

        for w in g.get_adj(v):
            if self.has_cycle():
                return

            if not self.visited[w]:
                self.edge_to[w] = v
                self.dfs(g, v, w)
            elif w != u:
                x = v
                while x != w:
                    self.cycle.append(x)
                    x = self.edge_to[x]
                self.cycle.append(w)
                self.cycle.append(v)

    # return true if the graph haas a cycle
    def has_cycle(self) -> bool:
        return len(self.cycle) > 0

    # return a cycle in the graph
    def get_cycle(self) -> list[int]:
        return self.cycle


class Dicycle:
    def __init__(self, g: Digraph):
        self.visited = [False] * g.V()
        self.edge_to = [None] * g.V()
        self.visiting = [False] * g.V()
        self.cycle = []

        for v in range(g.V()):
            if not self.visited[v]:
                self.dfs(g, v)

    # depth first search for finding cycle
    def dfs(self, g: Digraph, v: int):
        self.visited[v] = True
        self.visiting[v] = True

        for w in g.get_adj(v):
            if self.has_cycle():
                return

            if not self.visited[w]:
                self.edge_to[w] = v
                self.dfs(g, w)
            elif self.visiting[w]:
                q = Deque()

                x = v
                while x != w:
                    q.appendleft(x)
                    x = self.edge_to[x]
                q.appendleft(w)
                q.appendleft(v)

                self.cycle = list(q)

        self.visiting[v] = False

    # return true if the graph haas a cycle
    def has_cycle(self) -> bool:
        return len(self.cycle) > 0

    # return a cycle in the graph
    def get_cycle(self) -> list[int]:
        return self.cycle


class Eulerian:
    # eulerian path: a path that uses every edge in the graph exactly once
    class Edge:
        def __init__(self, v: int, w: int):
            self.v = v
            self.w = w
            self.is_used = False

        def other(self, v) -> int:
            if v == self.v:
                return self.w
            elif v == self.w:
                return self.v
            else:
                raise Exception("invalid endpoint")

    def __init__(self, g: Graph):
        self.path = None
        self.cycle = None
        self.adj = [[] for _ in range(g.V())]

        # find petential start points where the degree of vertex is odd or any vertex with degree > 0
        odd_degree_vertices_num = 0
        s = -1  # start vertex
        for v in range(g.V()):
            if g.get_degree(v) % 2 > 0:
                odd_degree_vertices_num += 1
                s = v
        if s < 0:
            for v in range(g.V()):
                if g.get_degree(v) > 0:
                    s = v
                    break

        # special case if the graph has no edge
        if s < 0:
            s = 0

        # eulerian path does not exist if more than two vertices has odd degree
        if odd_degree_vertices_num > 2:
            return

        # build adjencent list with Edge class
        for v in range(g.V()):
            self_loop = 0
            for w in g.get_adj(v):
                edge = self.Edge(v, w)

                # avoid exploring copies of an edge v-w
                if v == w:
                    if self_loop % 2 == 0:
                        self.adj[v].append(edge)
                        self.adj[w].append(edge)
                    self_loop += 1
                elif v < w:
                    self.adj[v].append(edge)
                    self.adj[w].append(edge)

        path, cycle = Deque(), Deque()
        self.dfs(s, path, cycle)

        if len(path) == g.E() + 1:
            self.path = path

        if odd_degree_vertices_num == 0 and len(cycle) == g.E() + 1:
            self.cycle = cycle

    def dfs(self, v: int, path: Deque, cycle: Deque):
        for edge in self.adj[v]:
            if not edge.is_used:
                edge.is_used = True
                self.dfs(edge.other(v), path, cycle)
        path.appendleft(v)
        cycle.appendleft(v)

    # return the vertices on an Eulerian path
    def get_path(self) -> list[int]:
        return list(self.path)

    # return true if the graph has an Eulerian path
    def has_eulerian_path(self) -> bool:
        return self.path != None

    # return the vertices on an Eulerian cycle
    def get_cycle(self) -> list[int]:
        return list(self.cycle)

    # return true if the graph has an Eulerian cycle
    def has_eulerian_cycle(self) -> bool:
        return self.cycle != None


class DiEulerian:
    # eulerian path: a path that uses every edge in the graph exactly once
    class Edge:
        def __init__(self, v: int, w: int):
            self.v = v
            self.w = w
            self.is_used = False

        def other(self, v) -> int:
            if v == self.v:
                return self.w
            elif v == self.w:
                return self.v
            else:
                raise Exception("invalid endpoint")

    # eulerian path: a path that uses every edge in the graph exactly once
    def __init__(self, g: Digraph):
        self.adj = [[] for _ in range(g.V())]
        self.path = None
        self.cycle = None

        # find petential start points where the vertex's out degree > in degree
        # or any vertex out degree > 0
        s, deficit = -1, 0
        no_cycle = False
        for v in range(g.V()):
            if g.get_outdegree(v) > g.get_indegree(v):
                no_cycle = True
                deficit += g.get_outdegree(v) > g.get_indegree(v)
                s = v

        # eulerian path/cycle not exist
        if deficit > 1:
            return

        # special case if graph has no edge
        if s < 0:
            s = 0

        # build adjencent list with Edge class
        for v in range(g.V()):
            for w in g.get_adj(v):
                self.adj[v].append(self.Edge(v, w))

        path, cycle = Deque(), Deque()
        self.dfs(g, s, path, cycle)

        if len(path) == g.E() + 1:
            self.path = path

        if not no_cycle and len(cycle) == g.E() + 1:
            self.cycle = cycle

    def dfs(self, g: Digraph, v: int, path: Deque, cycle: Deque):
        for edge in self.adj[v]:
            if not edge.is_used:
                edge.is_used = True
                self.dfs(g, edge.other(v), path, cycle)
        path.appendleft(v)
        cycle.appendleft(v)

    # return the vertices on an Eulerian path
    def get_path(self) -> list[int]:
        return list(self.path)

    # return true if the graph has an Eulerian path
    def has_eulerian_path(self) -> bool:
        return self.path != None

    # return the vertices on an Eulerian cycle
    def get_cycle(self) -> list[int]:
        return list(self.cycle)

    # return true if the graph has an Eulerian cycle
    def has_eulerian_cycle(self) -> bool:
        return self.cycle != None


if __name__ == '__main__':
    with open('input/graph.txt', 'r') as fin:
        v = int(fin.readline().strip())
        e = int(fin.readline().strip())

        graph = Graph(v)

        for i in range(e):
            p, q = [int(x) for x in fin.readline().strip().split()]
            graph.add_edge(p, q)

        assert graph.V() == 13 and graph.E() == 13, f'{graph.V()} vertices, {graph.E()} edges'
        adj_list = {
            0: set([1, 2, 5,  6]),
            1: set([0]),
            2: set([0]),
            3: set([4, 5]),
            4: set([3, 5, 6]),
            5: set([0, 3, 4]),
            6: set([0, 4]),
            7: set([8]),
            8: set([7]),
            9: set([10, 11, 12]),
            10: set([9]),
            11: set([9, 12]),
            12: set([9, 11])
        }
        for i in range(graph.V()):
            assert adj_list[i] == set(graph.get_adj(i)), f'{i}: {" ".join(map(str, graph.get_adj(i)))}'

    with open('input/digraph.txt', 'r') as fin:
        v = int(fin.readline().strip())
        e = int(fin.readline().strip())

        digraph = Digraph(v)

        for i in range(e):
            p, q = [int(x) for x in fin.readline().strip().split()]
            digraph.add_edge(p, q)

        assert digraph.V() == 13 and digraph.E() == 22, f'{digraph.V()} vertices, {digraph.E()} edges'
        adj_list = {
            0: set([1, 5]),
            1: set(),
            2: set([0, 3]),
            3: set([2, 5]),
            4: set([2, 3]),
            5: set([4]),
            6: set([0, 4, 8, 9]),
            7: set([6, 9]),
            8: set([6]),
            9: set([10, 11]),
            10: set([12]),
            11: set([4, 12]),
            12: set([9])
        }
        for i in range(digraph.V()):
            assert adj_list[i] == set(digraph.get_adj(i)), f'{i}: {" ".join(map(str, digraph.get_adj(i)))}'

    with open('input/dfs_paths.txt', 'r') as fin:
        v = int(fin.readline().strip())
        e = int(fin.readline().strip())

        graph = Graph(v)

        for i in range(e):
            p, q = [int(x) for x in fin.readline().strip().split()]
            graph.add_edge(p, q)

        dfs_paths = DepthFirstPaths(graph, 0)

        paths = {
            0: [0],
            1: [0, 2, 1],
            2: [0, 2],
            3: [0, 2, 3],
            4: [0, 2, 3, 4],
            5: [0, 2, 3, 5]
        }
        for v, ps in paths.items():
            assert dfs_paths.has_path_to(v) and dfs_paths.get_path_to(
                v) == ps, f'path_to({v})={dfs_paths.get_path_to(v)} is not correct'

    with open('input/bfs_paths.txt', 'r') as fin:
        v = int(fin.readline().strip())
        e = int(fin.readline().strip())

        graph = Graph(v)

        for i in range(e):
            p, q = [int(x) for x in fin.readline().strip().split()]
            graph.add_edge(p, q)

        bfs_paths = BreadthFirstPaths(graph, [0])

        paths = {
            0: [0],
            1: [0, 1],
            2: [0, 2],
            3: [0, 2, 3],
            4: [0, 2, 4],
            5: [0, 5]
        }
        for v, ps in paths.items():
            assert bfs_paths.has_path_to(v) and bfs_paths.get_path_to(v) == ps, f'path_to({v}) is not correct'
            assert bfs_paths.get_dist_to(v) == (len(ps) - 1), f'dist_to({v}) is not correct'

    with open('input/dfs_order.txt', 'r') as fin:
        v = int(fin.readline().strip())
        e = int(fin.readline().strip())

        digraph = Digraph(v)

        for i in range(e):
            p, q = [int(x) for x in fin.readline().strip().split()]
            digraph.add_edge(p, q)

        dfs_order = DepthFirstOrder(digraph)

        preorder = [0, 5, 4, 1, 6, 9, 11, 12, 10, 2, 3, 7, 8]
        postorder = [4, 5, 1, 12, 11, 10, 9, 6, 0, 3, 2, 7, 8]

        assert dfs_order.get_pre() == preorder, f'preorder is not correct'
        assert dfs_order.get_post() == postorder, f'postorder is not correct'
        assert dfs_order.get_reverse_post() == list(reversed(postorder)), f'reversed postorder is not correct'

    with open('input/cc.txt', 'r') as fin:
        v = int(fin.readline().strip())
        e = int(fin.readline().strip())

        graph = Graph(v)

        for i in range(e):
            p, q = [int(x) for x in fin.readline().strip().split()]
            graph.add_edge(p, q)

        cc = ConnectedComponent(graph)

        num_components = 3
        components = {
            0: set([0, 1, 2, 3, 4, 5, 6]),
            1: set([7, 8]),
            2: set([9, 10, 11, 12])
        }

        assert cc.get_count() == num_components, f'# of connected components is not correct'
        for i in range(v):
            cid = cc.get_id(i)
            assert i in components[cid], f'{i} is not in component {cid}'
            assert cc.get_size(i) == len(components[cid]), f'component size of {cid} is not correct'

    with open('input/scc.txt', 'r') as fin:
        v = int(fin.readline().strip())
        e = int(fin.readline().strip())

        digraph = Digraph(v)

        for i in range(e):
            p, q = [int(x) for x in fin.readline().strip().split()]
            digraph.add_edge(p, q)

        scc = StrongConnectedComponents(digraph)

        num_components = 5
        components = {
            0: set([1]),
            1: set([0, 2, 3, 4, 5]),
            2: set([9, 10, 11, 12]),
            3: set([6, 8]),
            4: set([7])
        }

        assert scc.get_count() == num_components, f'# of strong connected components is not correct'
        for i in range(v):
            cid = scc.get_id(i)
            assert i in components[cid], f'{i} is not in component {cid}'
            assert scc.get_size(i) == len(components[cid]), f'component size of {cid} is not correct'

    with open('input/cycle.txt', 'r') as fin:
        v = int(fin.readline().strip())
        e = int(fin.readline().strip())

        graph = Graph(v)

        for i in range(e):
            p, q = [int(x) for x in fin.readline().strip().split()]
            graph.add_edge(p, q)

        cycle = Cycle(graph)

        c_path = [3, 4, 5, 3]

        assert cycle.has_cycle(), f'graph has a cycle'
        assert cycle.get_cycle() == c_path or list(reversed(cycle.get_cycle())) == c_path, f'cycle path is not correct'

    with open('input/dicycle.txt', 'r') as fin:
        v = int(fin.readline().strip())
        e = int(fin.readline().strip())

        digraph = Digraph(v)

        for i in range(e):
            p, q = [int(x) for x in fin.readline().strip().split()]
            digraph.add_edge(p, q)

        dicycle = Dicycle(digraph)

        c_path = [3, 5, 4, 3]

        assert dicycle.has_cycle(), f'graph has a cycle'
        assert dicycle.get_cycle() == c_path, f'cycle path is not correct'

    with open('input/eulerian.txt', 'r') as fin:
        v = int(fin.readline().strip())
        e = int(fin.readline().strip())

        graph = Graph(v)

        for i in range(e):
            p, q = [int(x) for x in fin.readline().strip().split()]
            graph.add_edge(p, q)

        eulerian = Eulerian(graph)
        path = [0, 1, 3, 4, 2, 0]

        assert eulerian.has_eulerian_path(), f'eulerian path does exist'
        assert eulerian.get_path() == path, f'eulerian path is not correct'

        assert eulerian.has_eulerian_cycle(), f'eulerian cycle does exist'
        assert eulerian.get_cycle() == path, f'eulerian cycle is not correct'

    with open('input/dieulerian.txt', 'r') as fin:
        v = int(fin.readline().strip())
        e = int(fin.readline().strip())

        digraph = Digraph(v)

        for i in range(e):
            p, q = [int(x) for x in fin.readline().strip().split()]
            digraph.add_edge(p, q)

        di_eulerian = DiEulerian(digraph)
        path = [0, 1, 3, 4, 3, 1, 4, 2, 0]

        assert di_eulerian.has_eulerian_path(), f'eulerian path does exist'
        assert di_eulerian.get_path() == path, f'eulerian path is not correct'

        assert di_eulerian.has_eulerian_cycle(), f'eulerian cycle does exist'
        assert di_eulerian.get_cycle() == path, f'eulerian cycle is not correct'
