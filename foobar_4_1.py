class Node:
    def __init__(self, val):
        self.data = val
        self.adj = []


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


class MaxFlowSolver:
    def __init__(self, graph):
        self.graph = graph
        self.max_flow = 0


def solution(entrances, exits, path):
    graph = Graph(path, entrances, exits)
