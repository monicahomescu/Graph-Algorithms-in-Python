from graph import Graph, read_graph, write_graph
import random


class Main:

    def __init__(self):
        self._graph = Graph(0, 0)
        self._copy = Graph(0, 0)

    def no_vertices_ui(self):
        print("The number of vertices is " + str(self._graph.no_vertices) + "!")

    def parse_vertices_ui(self):
        if len(self._graph.parse_vertices()) == 0:
            print("There are no vertices!")
        else:
            print("The vertices are " + str(self._graph.parse_vertices()) + "!")

    def verify_edge_ui(self):
        x = int(input("Enter the start vertex: "))
        y = int(input("Enter the end vertex: "))
        if self._graph.verify_edge(x, y):
            print("The edge exists!")
        else:
            print("The edge doesn't exist!")

    def in_degree_ui(self):
        x = int(input("Enter the vertex: "))
        if self._graph.in_degree(x) == -1:
            print("The vertex doesn't exist!")
        else:
            print("The in degree is " + str(self._graph.in_degree(x)) + "!")

    def out_degree_ui(self):
        x = int(input("Enter the vertex: "))
        if self._graph.out_degree(x) == -1:
            print("The vertex doesn't exist!")
        else:
            print("The out degree is " + str(self._graph.out_degree(x)) + "!")

    def parse_outbound_ui(self):
        x = int(input("Enter the vertex: "))
        if self._graph.parse_outbound(x) == -1:
            print("The vertex doesn't exist!")
        elif len(self._graph.parse_outbound(x)) == 0:
            print("There are no outbound edges!")
        else:
            print("The outbound edges are " + str(self._graph.parse_outbound(x)) + "!")

    def parse_inbound_ui(self):
        x = int(input("Enter the vertex: "))
        if self._graph.parse_inbound(x) == -1:
            print("The vertex doesn't exist!")
        elif len(self._graph.parse_inbound(x)) == 0:
            print("There are no inbound edges!")
        else:
            print("The inbound edges are " + str(self._graph.parse_inbound(x)) + "!")

    def retrieve_info_ui(self):
        x = int(input("Enter the start vertex: "))
        y = int(input("Enter the end vertex: "))
        if not self._graph.verify_edge(x, y):
            print("The edge doesn't exist!")
        else:
            print("The information is " + str(self._graph.retrieve_info(x, y)) + "!")

    def modify_info_ui(self):
        x = int(input("Enter the start vertex: "))
        y = int(input("Enter the end vertex: "))
        i = int(input("Enter the information: "))
        res = self._graph.modify_info(x, y, i)
        if not res:
            print("The edge doesn't exist!")
        else:
            print("The information was modified!")

    def add_edge_ui(self):
        x = int(input("Enter the start vertex: "))
        y = int(input("Enter the end vertex: "))
        i = int(input("Enter the information: "))
        res = self._graph.add_edge(x, y, i)
        if res == -1:
            print("The vertex input is incorrect!")
        elif res == 0:
            print("The edge already exists!")
        else:
            print("The edge was added!")

    def remove_edge_ui(self):
        x = int(input("Enter the start vertex: "))
        y = int(input("Enter the end vertex: "))
        res = self._graph.remove_edge(x, y)
        if not res:
            print("The edge doesn't exist!")
        else:
            print("The edge was removed!")

    def add_vertex_ui(self):
        x = int(input("Enter the vertex: "))
        res = self._graph.add_vertex(x)
        if not res:
            print("The vertex already exists!")
        else:
            print("The vertex was added!")

    def remove_vertex_ui(self):
        x = int(input("Enter the vertex: "))
        res = self._graph.remove_vertex(x)
        if not res:
            print("The vertex doesn't exist!")
        else:
            print("The vertex was removed!")

    def copy_graph_ui(self):
        self._copy = self._graph.copy_graph()
        print("The graph was copied!")

    def read_graph_ui(self):
        filename = input("Enter the file to read out of: ")
        graph = read_graph(filename)
        self._graph = graph
        print("The graph was read!")

    def write_graph_ui(self):
        file_name = "output.txt"
        write_graph(self._graph, file_name)
        print("The graph was written!")

    def random_graph_ui(self):
        n = random.randint(1, 99)
        m = random.randint(0, n*(n-1))
        graph = Graph(n, m)
        while m > 0:
            x = random.randrange(n)
            y = random.randrange(n)
            i = random.randint(0, 99)
            if not graph.verify_edge(x, y):
                graph.add_edge(x, y, i)
                m -= 1
        self._graph = graph
        print("The random graph was generated!")

    def use_copy_ui(self):
        self._graph = self._copy
        print("The graph was replaced by the current copy!")

    def dag_ui(self):
        sorted = self._graph.topological_sorting()
        if len(sorted) == 0:
            print("The graph is not a DAG!")
        else:
            print("The topological sorting is: " + str(sorted))
            start = int(input("Enter the start vertex: "))
            end = int(input("Enter the end vertex: "))
            if start not in self._graph.parse_vertices() or end not in self._graph.parse_vertices():
                print("The vertex input is incorrect!")
            else:
                dist, prev = self._graph.highest_cost_path(start, end)
                if dist == float("-inf"):
                    print("There is no walk between the vertices!")
                else:
                    path = []
                    vertex = end
                    path.append(vertex)
                    while prev[vertex] != -1:
                        path.append(prev[vertex])
                        vertex = prev[vertex]
                    print("The highest cost path is: " + str(dist)[:-2])
                    path.reverse()
                    print("The path is: " + str(path))

    @staticmethod
    def print_menu():
        print("-------------------------------------------------------------------")
        print("0 - exit program")
        print("1 - get number of vertices")
        print("2 - parse vertices")
        print("3 - verify edge")
        print("4 - get in degree of vertex")
        print("5 - get out degree of vertex")
        print("6 - parse outbound edges of vertex")
        print("7 - parse inbound edges of vertex")
        print("8 - retrieve information of edge")
        print("9 - modify information of edge")
        print("10 - add edge")
        print("11 - remove edge")
        print("12 - add vertex")
        print("13 - remove vertex")
        print("14 - copy graph")
        print("15 - read graph from text file")
        print("16 - write graph from text file")
        print("17 - create random graph")
        print("18 - use current copy")
        print("19 - if graph is DAG, sort topologically and find highest cost path")
        print("-------------------------------------------------------------------")

    def start(self):
        commands = {
            "1": self.no_vertices_ui, "2": self.parse_vertices_ui, "3": self.verify_edge_ui, "4": self.in_degree_ui,
            "5": self.out_degree_ui, "6": self.parse_outbound_ui, "7": self.parse_inbound_ui, "8": self.retrieve_info_ui,
            "9": self.modify_info_ui, "10": self.add_edge_ui, "11": self.remove_edge_ui, "12": self.add_vertex_ui,
            "13": self.remove_vertex_ui, "14": self.copy_graph_ui, "15": self.read_graph_ui, "16": self.write_graph_ui,
            "17": self.random_graph_ui, "18": self.use_copy_ui, "19": self.dag_ui
                    }
        while True:
            self.print_menu()
            c = input("Enter the command: ")
            if c == "0":
                break
            elif c in commands:
                commands[c]()
            else:
                print("The command doesn't exist!")


Main().start()
