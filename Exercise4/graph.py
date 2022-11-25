import copy
import queue


class Graph:

    def __init__(self, no_vertices, no_edges):
        self._no_vertices = no_vertices
        self._no_edges = no_edges
        self._dict_in = {}
        self._dict_out = {}
        self._dict_info = {}
        for x in range(no_vertices):
            self._dict_in[x] = []
            self._dict_out[x] = []

    @property
    def no_vertices(self):
        return self._no_vertices

    def parse_vertices(self):
        return list(self._dict_out.keys())

    def verify_edge(self, x, y):
        if x not in self._dict_in.keys() or y not in self._dict_in.keys():
            return False
        if x in self._dict_in[y]:
            return True
        if y in self._dict_out[x]:
            return True
        return False

    def in_degree(self, x):
        if x not in self._dict_in.keys():
            return -1
        return len(self._dict_in[x])

    def out_degree(self, x):
        if x not in self._dict_out.keys():
            return -1
        return len(self._dict_out[x])

    def parse_outbound(self, x):
        if x not in self._dict_out.keys():
            return -1
        return list(self._dict_out[x])

    def parse_inbound(self, x):
        if x not in self._dict_in.keys():
            return -1
        return list(self._dict_in[x])

    def retrieve_info(self, x, y):
        return self._dict_info[(x, y)]

    def modify_info(self, x, y, i):
        if (x, y) not in self._dict_info.keys():
            return False
        self._dict_info[(x, y)] = i
        return True

    def add_edge(self, x, y, i):
        if x not in self._dict_in.keys() or y not in self._dict_in.keys():
            return -1
        if x in self._dict_in[y]:
            return 0
        if y in self._dict_out[x]:
            return 0
        if (x, y) in self._dict_info.keys():
            return 0
        self._dict_in[y].append(x)
        self._dict_out[x].append(y)
        self._dict_info[(x, y)] = i
        self._no_edges += 1
        return 1

    def remove_edge(self, x, y):
        if x not in self._dict_in.keys() or y not in self._dict_in.keys() or x not in self._dict_out.keys() or y not \
                in self._dict_out.keys():
            return False
        if x not in self._dict_in[y]:
            return False
        if y not in self._dict_out[x]:
            return False
        if (x, y) not in self._dict_info.keys():
            return False
        self._dict_in[y].remove(x)
        self._dict_out[x].remove(y)
        self._dict_info.pop((x, y))
        self._no_edges -= 1
        return True

    def add_vertex(self, x):
        if x in self._dict_in.keys() and x in self._dict_out.keys():
            return False
        self._dict_in[x] = []
        self._dict_out[x] = []
        self._no_vertices += 1
        return True

    def remove_vertex(self, x):
        if x not in self._dict_in.keys() and x not in self._dict_out.keys():
            return False
        self._dict_in.pop(x)
        self._dict_out.pop(x)
        for k in self._dict_in.keys():
            if x in self._dict_in[k]:
                self._dict_in[k].remove(x)
        for k in self._dict_out.keys():
            if x in self._dict_out[k]:
                self._dict_out[k].remove(x)
        info = list(self._dict_info.keys())
        for k in info:
            if k[0] == x or k[1] == x:
                self._dict_info.pop(k)
                self._no_edges -= 1
        self._no_vertices -= 1
        return True

    def copy_graph(self):
        return copy.deepcopy(self)

    @property
    def no_edges(self):
        return self._no_edges

    @property
    def dict_in(self):
        return self._dict_in

    @property
    def dict_out(self):
        return self._dict_out

    @property
    def dict_info(self):
        return self._dict_info

    def topological_sorting(self):
        sorted = []
        q = queue.Queue()
        count = {}
        for x in self.parse_vertices():
            count[x] = self.in_degree(x)
            if count[x] == 0:
                q.put(x)
        while not q.empty():
            x = q.get()
            sorted.append(x)
            for y in self._dict_out[x]:
                count[y] -= 1
                if count[y] == 0:
                    q.put(y)
        if len(sorted) < len(self.parse_vertices()):
            sorted = []
        return sorted

    def highest_cost_path(self, start, end):
        sorted = self.topological_sorting()
        dist = {}
        path = {}
        for x in sorted:
            dist[x] = float('-inf')
            path[x] = -1
        dist[start] = 0
        for x in sorted:
            if x == end:
                break
            for y in self._dict_out[x]:
                if dist[y] < dist[x] + self._dict_info[(x, y)]:
                    dist[y] = dist[x] + self._dict_info[(x, y)]
                    path[y] = x
        return float(dist[end]), path


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
        graph.dict_in[y].append(x)
        graph.dict_out[x].append(y)
        graph.dict_info[(x, y)] = i
    f.close()
    return graph


def write_graph(graph, file_name):
    f = open(file_name, "w")
    line = str(graph.no_vertices) + ' ' + str(graph.no_edges) + '\n'
    f.write(line)
    for i in graph.dict_info.keys():
        line = str(i[0]) + ' ' + str(i[1]) + ' ' + str(graph.dict_info[i]) + '\n'
        f.write(line)
    for i in graph.dict_in.keys():
        if len(graph.dict_in[i]) == 0 and len(graph.dict_out[i]) == 0:
            line = str(i) + '\n'
            f.write(line)
    f.close()
