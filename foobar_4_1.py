import sys


class Node:
    def __init__(self, val, parent):
        self.data = val
        self.adj = []
        self.parent = parent

    def add_edge(self, edge):
        self.adj.append(edge)

    def __eq__(self, other_node):
        return self.data == other_node.data

    def __contains__(self, items):
        for item in items:
            if item == self:
                return True

        return False

    def __str__(self):
        return_str = ""

        if self.parent is None:
            return str(self.data)
        else:
            return_str = "{}".format(self.data)
            parent = self.parent
            while parent is not None:
                return_str = "{} <-- {}".format(return_str, parent.data)
                parent = parent.parent

        return return_str


class Edge:
    def __init__(self, start, end, capacity, flow=0):
        self.start_node = start
        self.end_node = end
        self.capacity = capacity
        self.flow = flow


class Graph:
    def __init__(self, path, entrances, exits):
        self.path = path
        self.entrances = entrances
        self.exits = exits
        self.vertices = {}
        self.edges = {}
        self.create_graph()

    def create_graph(self):
        for i in range(len(self.path)):
            if i not in self.vertices:
                node_start = Node(i, None)
                self.vertices[i] = node_start
            else:
                node_start = self.vertices[i]

            for j in range(len(self.path[0])):
                if self.path[i][j] != 0:
                    if j not in self.vertices:
                        node_end = Node(j, node_start)
                        self.vertices[j] = node_end
                    else:
                        node_end = self.vertices[j]
                        node_end.parent = node_start

                    if i not in self.edges:
                        edge = Edge(node_start, node_end, self.path[i][j],
                                    flow=0)
                        self.edges[i] = edge
                    else:
                        edge = self.edges[i]

                    node_start.add_edge(edge)

    def find_path(self, start, end):
        if start not in self.vertices and end not in self.vertices:
            print("No such vertices found")
            sys.exit(1)

        queue = []
        visited = []

        queue.append(self.vertices[start])

        while len(queue) != 0:
            node = queue.pop(0)
            print(node)
            visited.append(node)

            if node == self.vertices[end]:
                return node

            for edge in node.adj:
                if edge.end_node not in visited and edge.end_node not in queue:
                    queue.append(edge.end_node)

        return None

    def __str__(self):
        return_str = ""

        for val, node in self.vertices.items():
            for vert in node.adj:
                return_str += str(val) + " --> " + str(vert.end_node.data) \
                                + ", "
            return_str += "\n"

        return return_str


class Dinic():
    level = {}
    graph = None

    @classmethod
    def assign_level(cls):
        cls.level = {val: -1 for val in cls.graph.vertices.keys()}

        for start in cls.graph.entrances:
            node = cls.graph.vertices[start]

            cls.level[start] = 0
            queue = []

            queue.append(node)
            while len(queue) != 0:
                node = queue.pop(0)

                for edge in node.adj:
                    if cls.level[edge.end_node.data] < 0 \
                            and edge.flow < edge.capacity:
                        cls.level[edge.end_node.data] = \
                            cls.level[node.data] + 1
                        queue.append(edge.end_node)

        for end in cls.graph.exits:
            if cls.level[end] < 0:
                return False

        return True

    @classmethod
    def send_flow(cls, vert, flow):
        node = cls.graph.vertices[vert]

        if node in cls.graph.exits:
            return flow

        for edge in node.adj:
            if cls.level[edge.end_node.data] == cls.level[node.data] + 1 \
                    and edge.flow < edge.capacity:
                curr_flow = min(flow, edge.capacity - edge.flow)
                tmp_flow = cls.send_flow(cls.graph, edge.end_node, curr_flow)

                if tmp_flow > 0:
                    edge.flow -= tmp_flow
                    return tmp_flow
        return 0

    @classmethod
    def solve(cls, graph):
        total = 0
        cls.graph = graph

        MAX_POSSIBLE_FLOW = sum(list(map(sum, cls.graph.path)))

        while cls.assign_level():
            for vert in cls.graph.entrances:
                flow = cls.send_flow(
                                        cls.graph.vertices[vert],
                                        MAX_POSSIBLE_FLOW
                                    )

            while flow:
                total += flow

        return total


class MaxFlowSolver():
    graph = None
    max_flow = 0

    @classmethod
    def solve(cls, graph, method="Dinic"):
        cls.graph = graph
        if method == "Dinic":
            cls.max_flow = Dinic.solve(cls.graph)
            return cls.max_flow


def solution(entrances, exits, path):
    graph = Graph(path, entrances, exits)

    max_flow = MaxFlowSolver.solve(graph)

    print(max_flow)
    # print(graph)
    # print(graph.find_path(1, 4))


solution([0, 1], [4, 5], [
                            [0, 0, 4, 6, 0, 0],
                            [0, 0, 5, 2, 0, 0],
                            [0, 0, 0, 0, 4, 4],
                            [0, 0, 0, 0, 6, 6],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0]
                        ])
