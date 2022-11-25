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

    def degree_ui(self):
        x = int(input("Enter the vertex: "))
        if self._graph.degree(x) == -1:
            print("The vertex doesn't exist!")
        else:
            print("The degree is " + str(self._graph.degree(x)) + "!")

    def parse_edges_ui(self):
        x = int(input("Enter the vertex: "))
        if self._graph.parse_edges(x) == -1:
            print("The vertex doesn't exist!")
        elif len(self._graph.parse_edges(x)) == 0:
            print("There are no edges!")
        else:
            print("The edges are " + str(self._graph.parse_edges(x)) + "!")

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
        m = random.randint(0, int(n*(n-1)/2))
        graph = Graph(n, m)
        while m > 0:
            x = random.randrange(n)
            y = random.randrange(n)
            i = random.randint(0, 99)
            if not graph.verify_edge(x, y) and not graph.verify_edge(y, x):
                graph.add_edge(x, y, i)
                m -= 1
        self._graph = graph
        print("The random graph was generated!")

    def use_copy_ui(self):
        self._graph = self._copy
        print("The graph was replaced by the current copy!")

    def find_connected_components_ui(self):
        print("The connected components are:")
        components = self._graph.find_connected_components()
        for component in components:
            print(component)

    @staticmethod
    def print_menu():
        print("----------------------------------")
        print("0 - exit program")
        print("1 - get number of vertices")
        print("2 - parse vertices")
        print("3 - verify edge")
        print("4 - get degree of vertex")
        print("5 - parse edges of vertex")
        print("6 - retrieve information of edge")
        print("7 - modify information of edge")
        print("8 - add edge")
        print("9 - remove edge")
        print("10 - add vertex")
        print("11 - remove vertex")
        print("12 - copy graph")
        print("13 - read graph from text file")
        print("14 - write graph from text file")
        print("15 - create random graph")
        print("16 - use current copy")
        print("17 - find connected components")
        print("----------------------------------")

    def start(self):
        commands = {
            "1": self.no_vertices_ui, "2": self.parse_vertices_ui, "3": self.verify_edge_ui, "4": self.degree_ui,
            "5": self.parse_edges_ui, "6": self.retrieve_info_ui, "7": self.modify_info_ui, "8": self.add_edge_ui,
            "9": self.remove_edge_ui, "10": self.add_vertex_ui, "11": self.remove_vertex_ui, "12": self.copy_graph_ui,
            "13": self.read_graph_ui, "14": self.write_graph_ui, "15": self.random_graph_ui, "16": self.use_copy_ui,
            "17": self.find_connected_components_ui
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
