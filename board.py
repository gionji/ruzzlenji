
##
# a0 a1 a2 a3
# b0 b1 b2 b3
# c0 c1 c2 c3
# d0 d1 d2 d3
##


class Board:

    def __init__( self, init_string=None ):
        self.init_string = init_string
        self.__graph_dict = None
        self.__edges = None

    ## puo essere fatto in automatico per board di dimensione n
    def init_graph(self):
        self.__graph_dict = { "a0": ["a1", "b1", "b0"],
                  "a1": ["a0", "b0", "b1", "b2", "a2"],
                  "a2": ["a1", "a3", "b1", "b2", "b3"],
                  "a3": ["b3", "b2", "a2"],
                  "b0": ["a0", "a1", "b1", "c1", "c0"],
                  "b1": ["a0", "a1", "a2", "b0", "b2", "c0", "c1", "c2"],
                  "b2": ["a1", "a2", "a3", "b1", "b3", "c1", "c2", "c3"],
                  "b3": ["a2", "a3", "b2", "c2", "c3"],
                  "c0": ["b0", "b1", "c1", "d0", "d1", ],
                  "c1": ["b0", "b1", "b2", "c0", "c2",  "d0", "d1", "d2",],
                  "c2": ["b1", "b2", "b3", "c1", "c3","d1", "d2", "d3",],
                  "c3": [ "b2", "b3","c2", "d2", "d3", ],
                  "d0": [ "c0", "c1", "d1", ],
                  "d1": [ "c0", "c1", "c2", "d0", "d2", ],
                  "d2": [ "c1", "c2", "c3", "d1", "d3", ],
                  "d3": [ "c2", "c3", "d2", ]
                 }

    def generate_edges(self):
        edges = []
        for node in self.__graph_dict:
            for neighbour in self.__graph_dict[node]:
                edges.append((node, neighbour))
        self.__edges = edges
        return edges

    def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex
            in graph """
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex,
                                               end_vertex,
                                               path)
                if extended_path:
                    return extended_path
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to
            end_vertex in graph """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex,
                                                     end_vertex,
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.edges


