import copy
from random import choice


class Graph:

    def __init__(self, no_vertices, no_edges):
        self._no_vertices = no_vertices
        self._no_edges = no_edges
        self._vertices = []
        self._edges = {}
        self._info = {}
        for i in range(no_vertices):
            self._vertices.append(i)
            self._edges[i] = []

    @property
    def no_vertices(self):
        return self._no_vertices

    def parse_vertices(self):
        return self._vertices

    def verify_edge(self, x, y):
        if x not in self._vertices or y not in self._vertices:
            return False
        if x in self._edges[y] and y in self._edges[x]:
            return True
        return False

    def degree(self, x):
        if x not in self._vertices:
            return -1
        return len(self._edges[x])

    def parse_edges(self, x):
        if x not in self._vertices:
            return -1
        return list(self._edges[x])

    def retrieve_info(self, x, y):
        if (x, y) in self._info.keys():
            return self._info[(x, y)]
        elif (y, x) in self._info.keys():
            return self._info[(y, x)]

    def modify_info(self, x, y, i):
        if (x, y) not in self._info.keys() and (y, x) not in self._info.keys():
            return False
        if (x, y) in self._info.keys():
            self._info[(x, y)] = i
        elif (y, x) in self._info.keys():
            self._info[(y, x)] = i
        return True

    def add_edge(self, x, y, i):
        if x not in self._vertices or y not in self._vertices:
            return -1
        if x == y:
            return -1
        if x in self._edges[y] and y in self._edges[x]:
            return 0
        if (x, y) in self._info.keys() or (y, x) in self._info.keys():
            return 0
        self._edges[x].append(y)
        self._edges[y].append(x)
        self._info[(x, y)] = i
        self._no_edges += 1
        return 1

    def remove_edge(self, x, y):
        if x not in self._vertices or y not in self._vertices:
            return False
        if x == y:
            return False
        if x not in self._edges[y] or y not in self._edges[x]:
            return False
        if (x, y) not in self._info.keys() and (y, x) not in self._info.keys():
            return False
        self._edges[x].remove(y)
        self._edges[y].remove(x)
        if (x, y) in self._info.keys():
            self._info.pop((x, y))
        elif (y, x) in self._info.keys():
            self._info.pop((y, x))
        self._no_edges -= 1
        return True

    def add_vertex(self, x):
        if x in self._vertices:
            return False
        self._vertices.append(x)
        self._edges[x] = []
        self._no_vertices += 1
        return True

    def remove_vertex(self, x):
        if x not in self._vertices:
            return False
        self._vertices.remove(x)
        self._edges.pop(x)
        for k in self._edges.keys():
            if x in self._edges[k]:
                self._edges[k].remove(x)
                self._no_edges -= 1
        info_list = list(self._info.keys())
        for k in info_list:
            if k[0] == x or k[1] == x:
                self._info.pop(k)
        self._no_vertices -= 1
        return True

    def copy_graph(self):
        return copy.deepcopy(self)

    @property
    def no_edges(self):
        return self._no_edges

    @property
    def edges(self):
        return self._edges

    @property
    def info(self):
        return self._info

    def find_covering(self):
        visited = [False] * self.no_vertices
        for x in range(self.no_vertices):
            if not visited[x]:
                for y in self.edges[x]:
                    if not visited[y]:
                        visited[y] = True
                        visited[x] = True
                        break
        for i in self._vertices:
            if visited[i]:
                print(i, end=" ")
        print()


def read_graph(file_name):
    f = open(file_name, "r")
    line = f.readline()
    line = line.strip().split()
    no_vertices = int(line[0])
    no_edges = int(line[1])
    graph = Graph(no_vertices, no_edges)
    for i in range(no_edges):
        line = f.readline()
        line = line.strip().split()
        x = int(line[0])
        y = int(line[1])
        i = int(line[2])
        graph.edges[x].append(y)
        graph.edges[y].append(x)
        graph.info[(x, y)] = i
    f.close()
    return graph


def write_graph(graph, file_name):
    f = open(file_name, "w")
    line = str(graph.no_vertices) + ' ' + str(graph.no_edges) + '\n'
    f.write(line)
    for x in graph.parse_vertices():
        line = str(x) + ' '
        f.write(line)
    line = '\n'
    f.write(line)
    edges = []
    for i in graph.edges:
        for j in graph.edges[i]:
            if (i, j) not in edges and (j, i) not in edges:
                if (i, j) in graph.info.keys():
                    edges.append((i, j, graph.info[(i, j)]))
                elif (j, i) in graph.info.keys():
                    edges.append((i, j, graph.info[j, i]))
    for x in edges:
        line = str(x[0]) + ' ' + str(x[1]) + ' ' + str(x[2]) + '\n'
        f.write(line)
    f.close()
