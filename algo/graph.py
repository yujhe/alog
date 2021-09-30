from typing import Deque


class Graph:
    def __init__(self, v):
        pass

    # return # of vertices
    def V(self) -> int:
        pass

    # return # of edges
    def E(self) -> int:
        pass

    # add edge between v and w
    def add_edge(self, v: int, w: int) -> None:
        pass

    # return the vertices adjacent to vertex v
    def get_adj(self, v: int) -> list[int]:
        pass

    # return the degree of vertex v
    def get_degree(self, v: int) -> int:
        pass


class Digraph:
    def __init__(self, v):
        pass

    # return # of vertices
    def V(self) -> int:
        pass

    # return # of edges
    def E(self) -> int:
        pass

    # add edge between v and w
    def add_edge(self, v: int, w: int) -> None:
        pass

    # return the vertices adjacent to vertex v
    def get_adj(self, v: int) -> list[int]:
        pass

    # return the indegree of vertex v
    def get_indegree(self, v: int) -> int:
        pass

    # return the outdegree of vertex v
    def get_outdegree(self, v: int) -> int:
        pass

    # return the reverse of the digraph
    def reverse(self):
        pass


class DepthFirstPaths:
    def __init__(self, g: Graph, s: int):
        pass

    # depth first search from v
    def dfs(self, g: Graph, v: int) -> None:
        pass

    # is there a path between source to v?
    def has_path_to(self, v: int) -> bool:
        pass

    # return a path between source to v
    def get_path_to(self, v: int) -> list[int]:
        pass


class BreadthFirstPaths:
    def __init__(self, g: Graph, ss: list[int]):
        pass

    # breadth first search from multiple sources
    def bfs(self, g: Graph, ss: list[int]) -> None:
        pass

    # is there a path between source to v
    def has_path_to(self, v: int) -> bool:
        pass

    # return the # of edges in a shortest path between source and v
    def get_dist_to(self, v: int) -> int:
        pass

    # return the shortest path between source and v
    def get_path_to(self, v: int) -> list[int]:
        pass


class DepthFirstOrder:
    def __init__(self, g: Digraph):
        pass

    # depth first search for a graph
    def dfs(self, g: Graph, v: int) -> None:
        pass

    # return the preorder number of v
    def get_preorder(self, v: int) -> int:
        pass

    # return the postorder number of v
    def get_postorder(self, v: int) -> int:
        pass

    # return the vertices in preorder
    def get_pre(self) -> list[int]:
        pass

    # return the vertices in postorder
    def get_post(self) -> list[int]:
        pass

    # return the vertices in reverse postorder
    def get_reverse_post(self) -> list[int]:
        pass


class ConnectedComponent:
    def __init__(self, g: Graph):
        pass

    # depth first search for a graph
    def dfs(self, g: Graph, v: int) -> None:
        pass

    # return true if v and w are in the same connected component
    def connected(self, v: int, w: int) -> bool:
        pass

    # return # of connected components
    def get_count(self) -> int:
        pass

    # return # of vertices in the connected component containing v
    def get_size(self, v) -> int:
        pass

    # return the component id of v
    def get_id(self, v: int) -> int:
        pass


class StrongConnectedComponents:
    def __init__(self, g: Digraph):
        pass

    # depth first seach for a graph
    def dfs(self, g: Digraph, v: int) -> None:
        pass

    # return true if v and w are in the same connected component
    def connected(self, v: int, w: int) -> bool:
        pass

    # return # of connected components
    def get_count(self) -> int:
        pass

    # return # of vertices in the connected component containing v
    def get_size(self, v) -> int:
        pass

    # return the component id of v
    def get_id(self, v: int) -> int:
        pass


class Cycle:
    def __init__(self, g: Graph):
        pass

    # depth first search from u to v
    def dfs(self, g: Graph, u: int, v: int) -> None:
        pass

    # return true if the graph haas a cycle
    def has_cycle(self) -> bool:
        pass

    # return a cycle in the graph
    def get_cycle(self) -> list[int]:
        pass


class Dicycle:
    def __init__(self, g: Digraph):
        pass

    # depth first search for finding cycle
    def dfs(self, g: Digraph, v: int):
        pass

    # return true if the graph haas a cycle
    def has_cycle(self) -> bool:
        pass

    # return a cycle in the graph
    def get_cycle(self) -> list[int]:
        pass


class Eulerian:
    # eulerian path: a path that uses every edge in the graph exactly once
    class Edge:
        def __init__(self, v: int, w: int):
            pass

        def other(self, v) -> int:
            pass

    def __init__(self, g: Graph):
        pass

        # find petential start points where the degree of vertex is odd or any vertex with degree > 0
        pass

        # special case if the graph has no edge
        pass

        # eulerian path does not exist if more than two vertices has odd degree
        pass

        # build adjencent list with Edge class
        pass

    def dfs(self, v: int, path: Deque, cycle: Deque):
        pass

    # return the vertices on an Eulerian path
    def get_path(self) -> list[int]:
        pass

    # return true if the graph has an Eulerian path
    def has_eulerian_path(self) -> bool:
        pass

    # return the vertices on an Eulerian cycle
    def get_cycle(self) -> list[int]:
        pass

    # return true if the graph has an Eulerian cycle
    def has_eulerian_cycle(self) -> bool:
        pass


class DiEulerian:
    # eulerian path: a path that uses every edge in the graph exactly once
    class Edge:
        def __init__(self, v: int, w: int):
            pass

        def other(self, v) -> int:
            pass

    # eulerian path: a path that uses every edge in the graph exactly once
    def __init__(self, g: Digraph):
        pass

        # find petential start points where the vertex's out degree > in degree
        # or any vertex out degree > 0
        pass

        # eulerian path/cycle not exist
        pass

        # special case if graph has no edge
        pass

        # build adjencent list with Edge class
        pass

    def dfs(self, g: Digraph, v: int, path: Deque, cycle: Deque):
        pass

    # return the vertices on an Eulerian path
    def get_path(self) -> list[int]:
        pass

    # return true if the graph has an Eulerian path
    def has_eulerian_path(self) -> bool:
        pass

    # return the vertices on an Eulerian cycle
    def get_cycle(self) -> list[int]:
        pass

    # return true if the graph has an Eulerian cycle
    def has_eulerian_cycle(self) -> bool:
        pass


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
